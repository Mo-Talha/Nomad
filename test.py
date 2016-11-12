import mongoengine
import time
from models.job import Job
from models.location import Location

import shared.secrets as secrets

if __name__ == "__main__":
    mongoengine.connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)

    for job in Job.objects:
        for l in job.location:
            if l.longitude == 0.0 and l.latitude == 0.0:
                location = Location(name=l.name)

                job.update(location=[location])
                time.sleep(2)
