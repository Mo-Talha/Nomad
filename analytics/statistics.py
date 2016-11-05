from models.job import Job


def get_programs_vs_jobs():
    program_vs_job_freq = Job.objects.item_frequencies('programs')
    return program_vs_job_freq


def get_jobs_vs_levels():
    jobs_vs_levels_freq = Job.objects.item_frequencies('levels')
    return jobs_vs_levels_freq
