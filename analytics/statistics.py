from mongoengine import connection

import models.job_keyword_type as keyword_type


def get_jobs_vs_programs():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {"_id": 0, "programs": 1}},
        {"$unwind": "$programs"},
        {"$group": {"_id": {
            "program": "$programs"
        }, "count": {"$sum": 1}}}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_levels():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {"_id": 0, "levels": 1}},
        {"$unwind": "$levels"},
        {"$group": {"_id": {
            "level": "$levels"
        }, "count": {"$sum": 1}}}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


def get_jobs_vs_terms():
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
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
    pipeline = [
        {"$redact": {
            "$cond": {
                "if": {"$eq": ["$deprecated", False]},
                "then": "$$KEEP",
                "else": "$$PRUNE"
            }
        }},
        {"$project": {"_id": 0, "location": 1}},
        {"$unwind": "$location"},
        {"$group": {"_id": {
            "location": "$location.name",
            "longitude": "$location.longitude",
            "latitude": "$location.latitude"
        }}}
    ]

    db = connection._get_db(reconnect=False)

    return db.job.aggregate(pipeline)


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


def get_jobs_vs_search_servers():
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
        {"$match": {"keywords.types": {"$in": [keyword_type.types["SEARCH_SRV"]]}}},
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
