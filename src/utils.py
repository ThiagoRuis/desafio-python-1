from datetime import datetime, timedelta
import time
from dateutil.rrule import rrule, MONTHLY

def compute_skills(skillset):
        computed_skills = []
        for skill in skillset:
            computed_time = []
            id, name = skill.split('-')
            for period in skillset[skill]:
                computed_time = compute_time(start_date=period['startDate'], end_date=period['endDate'], buffer=computed_time)

            computed_skills.append({
                "id": id,
                "name": name,
                "durationInMonths": len(computed_time)
            })
            
        return computed_skills

def compute_time(start_date, end_date, buffer):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=1)
    
    generated_months = [dt.strftime("%Y-%m") for dt in rrule(MONTHLY, dtstart=start, until=end)]
    return list(set(buffer + generated_months))


