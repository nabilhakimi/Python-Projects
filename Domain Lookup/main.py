import whois


sites = ["facebook.com", "spotify.com", "instagram.com", "youtube.com"]

companies = [whois.whois(s).org for s in sites]
creation_dates = [whois.whois(s).creation_date for s in sites]

print(companies)
print(creation_dates)
print(sites[creation_dates.index(min(creation_dates))])
