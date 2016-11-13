from mongoengine import connection

from models.job import Job


def get_programs_vs_jobs():
    program_vs_job_freq = Job.objects(deprecated=False).item_frequencies('programs')
    return program_vs_job_freq


def get_jobs_vs_levels():
    jobs_vs_levels_freq = Job.objects(deprecated=False).item_frequencies('levels')
    return jobs_vs_levels_freq


def get_jobs_vs_terms():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", "false"]},
                "then": "$$KEEP",
                "else": "$$DESCEND"
            }
        }},
        {"$project": {"year": '$year', "term": '$term'}},
        {"$group": {"_id": {
            "year": "$year",
            "term": "$term"
        }, "count": {"$sum": 1}}}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_locations():
    locations = Job.objects(deprecated=False).only('location').distinct(field="location")

    response = []

    for location in locations:
        response.append({
            'name': location.name,
            'longitude': location.longitude,
            'latitude': location.latitude
        })

    return response
