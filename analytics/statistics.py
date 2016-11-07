from mongoengine import connection

import googlemaps

from models.job import Job

import shared.secrets as secrets


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
    locations = Job.objects(deprecated=False).distinct(field="location")

    gmaps = googlemaps.Client(key=secrets.GOOGLE_MAPS_API_KEY)

    response = []

    for location in locations:
        geocode = gmaps.geocode(location)

        if type(geocode) is list and len(geocode) > 0:
            geocode = geocode[0]

            response.append({
                'name': location,
                'longitude': geocode['geometry']['location']['lng'],
                'latitude': geocode['geometry']['location']['lat']
            })

    return response
