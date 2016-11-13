from mongoengine import connection

import models.job_keyword_type as keyword_type
from models.job import Job


def get_jobs_vs_programs():
    job_vs_program_freq = Job.objects(deprecated=False).item_frequencies('programs')
    return job_vs_program_freq


def get_jobs_vs_levels():
    jobs_vs_levels_freq = Job.objects(deprecated=False).item_frequencies('levels')
    return jobs_vs_levels_freq


def get_jobs_vs_terms():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$DESCEND",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {"year": 1, "term": 1, "deprecated": 1}},
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


def get_jobs_vs_programming_languages():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["PROGRAMMING_LANG"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_databases():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["DB"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_operating_systems():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["OS"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_web_frameworks():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["WEB_FRWK"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_apache_frameworks():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["APACHE_FRWK"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_javascript_libraries():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["JS_LIB"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_css_frameworks():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {
            "_id": 0,
            "keywords": 1,
            "deprecated": 1
        }},
        {"$unwind": "$keywords"},
        {"$match": {"keywords.types": {"$in": [keyword_type.types["CSS_FRWK"]]}}},
        {"$group": {
            "_id": {
                "keyword": "$keywords.keyword",
                "types": "$keywords.types"
            },
            "count": {
                "$sum": 1
            }
        }}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)
