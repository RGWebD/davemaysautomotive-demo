# Facts for Dave Mays Automotive. Sources (captured 2026-11-25): Google Business Profile [GM], Facebook page [FB], door decal (Google photo g10), roadside sign (Reese's photo).
# See /workspace/davemays-research/notes.md. Nothing invented: no owner name as fact, no prices.
BASE = "https://rgwebd.github.io/davemaysautomotive-demo/"
NAME = "Dave Mays Automotive"
LEGAL = "Dave Mays Automotive, Inc."      # Facebook page name "Dave Mays Automotive, Inc"
PHONE = "(352) 372-7617"; TEL = "+13523727617"
STREET = "2905 NE 19th Dr"; CITY = "Gainesville"; REGION = "FL"; ZIP = "32609"
ADDR = f"{STREET}, {CITY}, {REGION} {ZIP}"
GEO = (29.678969, -82.2985268)
RATING = "4.6"; REVIEWS = 163
FB_PCT = 98; FB_N = 17
SINCE = 1975
DOOR = "We Get The Bugs Out of Your Car!"   # their door decal (g10)
MAPS = "https://maps.app.goo.gl/KBtcUF4ydyZZGLM8A"
MAPS_LONG = "https://www.google.com/maps/place/Dave+Mays+Automotive/@29.678969,-82.2985268,17z/data=!3m1!4b1!4m6!3m5!1s0x88e8a6a1b044c1bb:0x47dfdd13616fe318"
FB = "https://www.facebook.com/DaveMaysAutomotive/"
DIR = "https://www.google.com/maps/dir/?api=1&destination=Dave+Mays+Automotive,+2905+NE+19th+Dr,+Gainesville,+FL+32609"
# hours: index 0=Sun; minutes from midnight. Friday from the door decal + Google (holiday-week) -> flagged to confirm.
HOURS = [("Sunday",None,None),("Monday",450,1050),("Tuesday",450,1050),("Wednesday",450,1050),("Thursday",450,1050),("Friday",450,1020),("Saturday",None,None)]
HOLIDAYS = {"2026-11-26":"Thanksgiving","2026-11-27":"Black Friday","2026-12-24":"Christmas Eve","2026-12-25":"Christmas Day","2026-12-31":"New Year\u2019s Eve","2027-01-01":"New Year\u2019s Day"}
TOPICS = ["Honest mechanics","Loaner car","Friendly crew","Honest staff","Clean facility","Courteous staff","Affordable","Fast diagnosis","Brake job","Oil leak repair"]
WORK_ON = ["Classic cars","Day-to-day vehicles","Fleet vehicles"]   # FB bio

def fmt(m):
    h,mi=divmod(m,60); ap='AM' if h<12 else 'PM'; h=h%12 or 12
    return f"{h}:{mi:02d} {ap}"

REVIEWS_LIST = [
 dict(name="Tina Perkins", age="4 weeks ago", tag="Drove up from St. Pete", pull="The reason is because Dave Mays Auto is honest. And they treat you like family.",
  text="Amazing place to have your car worked on. I drove up from St Pete to have Dave Mays Auto look at my car. One might ask why come here when you pass many other places along the way and have places near me back where I live. The reason is because Dave Mays Auto is honest. And they treat you like family. Everyone that works there is so polite and really cares. And they make sure you are well taken care of. And they have the cleanest bathrooms. I dislike my dealership where I bought my car and really hate going to them so I bring it to Dave Mays to service and make sure my car is in good working order. This is the best place. You need someone that is honest and will treat you right go see everyone at Dave Mays Auto. They will take good care of you. The owners are great as well as the staff.  Thank you for everything! 5 \U0001F31F service always. Tina -St Petersburg Florida"),
 dict(name="James Crosby", age="a month ago", tag="Years of service", pull="They shoot it to you straight, the good, bad, or ugly.",
  text="By far the best in Gainesville. I\u2019ve been using Dave Mays for years now because they are the only ones you can trust with your vehicle. They shoot it to you straight, the good, bad, or ugly and will help you any way they can. Great Service for a fair price."),
 dict(name="Richard Harvey", age="a year ago", tag="Check engine light", pull="By 10:30 that morning the car was repaired.",
  text="My granddaughter's car was running rough and had a check engine light on. Took it in to Dave Mays without an appointment on Monday morning and by 10:30 that morning the car was repaired.\nThe charge was extremely reasonable and about 10 % of what the dealer had quoted.\nDave Mays has a great reputation for quality service at a reasonable cost.\nI say that reputation is well deserved!\nThese guys are very honest and will charge a fair price for the high quality  work  they do."),
 dict(name="Reid Wagner", age="a month ago", tag="Gainesville", pull="Reliable and honest service.",
  text="Great experience with Dave Mays Automotive in Gainesville. The staff was friendly, professional, and straightforward throughout the whole process. They communicated clearly, got the work done efficiently, and made everything easy. I\u2019d definitely recommend Dave Mays Automotive to anyone in Gainesville looking for reliable and honest service."),
 dict(name="Karen Swinea", age="a year ago", tag="Maintenance + loaner", pull="They also have a loaner vehicle so you don't have to miss time off work.",
  text="Great experience with Dave Mays! I've neglected some routine maintenance on my vehicle and needed to get some work done. The owners were so helpful is diagnosing what needed to be done first and worked with me to fit it into my budget. They also have a loaner vehicle so you don't have to miss time off work. Very professional and great customer service. I'll be back!"),
 dict(name="Pandora Rose", age="edited a month ago", tag="Looked out for me", pull="I really appreciate that Dave Mays took the time to research the issue and look out for me.",
  text="I had a check engine light come on for the second time. Before I even got to Dave Mays, they had researched my issue and had a solution ready to go. They found a turbocharger problem that was covered by a special extended manufacturer coverage and referred me to the Chevrolet dealership rather than having me pay for the repair myself. Chevrolet replaced the turbocharger at no charge. I really appreciate that Dave Mays took the time to research the issue and look out for me as a customer."),
 dict(name="Steven Murphy", age="4 months ago", tag="Rims + tires", pull="I don't feel like they're trying to scam me like other mechanics.",
  text="I highly recommend Dave Mays.tgey installed new rims and tires for me. Super friendly staff, very knowledgeable, and I don't feel like they're trying to scam me like other mechanics. When they told me what was wrong with my car they offered to sell me what I needed or offered an alternative of getting stuff myself and they would fix it for me. Overall just a very pleasant experience. Will be back here when it's needed."),
 dict(name="rene morrissey", age="2 months ago", tag="Budget-friendly options", pull="Giving a range of repair options and timing to accommodate budgets.",
  text="Many years of consistently excellent service. Especially notable for giving a range of repair options and timing to accommodate budgets, including steering away from costly repairs or parts that might be \u201crecommended\u201d but aren\u2019t worth the price difference. Also notable for anticipating future repairs that allows for budgeting."),
 dict(name="Jay Kalinowski", age="a month ago", tag="The whole crew", pull="The best service, honest, dependable.",
  text="Brian, Janeina & Alex and the rest of the crew provide the best service, honest, dependable. Take all my cars there now."),
 dict(name="David Harrison", age="a month ago", tag="25 years", pull="Great place for honest repairs.",
  text="Great place for honest repairs.  Enjoyed 25 years of knowing Brian.   Keep up the great work!!"),
]
EXCERPTS = [  # truncated in the Google list: shown as excerpts only, never as full reviews
 dict(name="Erin King", text="We've taken all 6 of our cars to them over the course of almost 30 years\u2026"),
 dict(name="Paul Theus", text="Our company brings our fleet vehicles here for service\u2026 Fair, honest , efficient , great communications."),
]

# services: key, title, photo, inset, short, long, bullets, proof(review name, quote), icon
SVC = [
 ("diag","Diagnostics &amp; check-engine lights","f08",None,"Warning light on? We find the cause and tell you straight.",
  "Engine diagnostics is where most visits start. We track down why the light is on or why it\u2019s running rough, then explain what we found and what it will take, before any work begins.",
  ["Check-engine &amp; warning lights","Running rough, stalling, hesitation","Oil leaks","Fast, clear diagnosis"],
  ("Richard Harvey","Took it in without an appointment on Monday morning and by 10:30 that morning the car was repaired."),"engine"),
 ("brakes","Brakes, steering &amp; suspension","f07",None,"Stops that feel right and a car that drives straight.",
  "Brake jobs, steering and suspension work on our lifts: noises, pulling, vibration or a soft pedal. You get the options and the reasons, not a scare list.",
  ["Brake jobs","Steering &amp; suspension","Noises, pulling &amp; vibration"],
  ("rene morrissey","Steering away from costly repairs or parts that might be \u201crecommended\u201d but aren\u2019t worth the price difference."),"brake"),
 ("tires","Tires, wheels &amp; alignment","g09",None,"New rubber, new rims and a straight, true alignment.",
  "Tire and wheel installs plus wheel alignment on our alignment rack, so your new tires wear evenly and the wheel sits straight.",
  ["Tires","Wheel alignment","Rims &amp; wheels"],
  ("Steven Murphy","They installed new rims and tires for me. Super friendly staff, very knowledgeable."),"tire"),
 ("maint","Oil changes &amp; maintenance","f01",None,"Oil, filters and the routine work that keeps it running.",
  "Oil changes, air and cabin filters and general maintenance. Fallen behind? We\u2019ll sort out what matters first and help you plan the rest around your budget.",
  ["Oil changes","Air &amp; cabin filters","General repairs &amp; maintenance","Planning ahead for future repairs"],
  ("Karen Swinea","The owners were so helpful is diagnosing what needed to be done first and worked with me to fit it into my budget."),"oil"),
 ("engine","Engine, electrical &amp; battery","g03",None,"From a dead battery to engine repair.",
  "Engine repair, electrical problems and batteries. We test before we replace, so you\u2019re paying to fix the actual problem.",
  ["Engine repair","Electrical","Batteries"],
  ("Pandora Rose","Before I even got to Dave Mays, they had researched my issue and had a solution ready to go."),"battery"),
 ("ac","A/C, transmission &amp; exhaust","f11",None,"Cold air in a Florida summer, smooth shifts, a quiet exhaust.",
  "Air-conditioning service, transmission work and exhaust repair: the jobs Gainesville drivers can\u2019t put off for long.",
  ["Air conditioning","Transmission","Exhaust"],
  ("Reid Wagner","They communicated clearly, got the work done efficiently, and made everything easy."),"snow"),
 ("fleet","Classic cars, daily drivers &amp; fleets","g08","f10","Old iron, the family car and the company trucks.",
  "We work on classic cars, day-to-day vehicles and fleet vehicles. Local businesses bring their fleets here, and families bring every car in the driveway.",
  ["Classic cars","Day-to-day vehicles","Fleet vehicles"],
  ("Paul Theus","Our company brings our fleet vehicles here for service\u2026 Fair, honest , efficient , great communications."),"truck"),
]

# dashboard lights (home): key, label, colour, what it means (general), what we do, service key
DASH = [
 ("engine","Check engine","amber","Your car\u2019s computer has logged a fault: anything from a loose gas cap to a misfire.","We read the codes, test the cause and tell you straight what it needs.","diag"),
 ("battery","Battery / charging","red","The charging system isn\u2019t keeping up: battery, alternator or wiring.","Battery and electrical testing before anything gets replaced.","engine"),
 ("brake","Brake system","red","Low brake fluid, worn pads or the parking brake is still on.","Brake inspection and brake jobs on our lifts.","brakes"),
 ("oil","Oil pressure","red","Low oil level or pressure. Pull over and don\u2019t keep driving on it.","Oil changes, leak checks and oil leak repair.","maint"),
 ("temp","Engine temperature","red","Running hot: coolant, thermostat, fan or water pump.","Diagnosis first, then the repair that fixes it.","diag"),
 ("tire","Tire pressure","amber","One or more tires is low, or the sensor needs attention.","Tires, wheels and alignment.","tires"),
 ("snow","A/C blowing warm","teal","Not a dash light, but in Gainesville it may as well be one.","A/C service and repair.","ac"),
 ("steer","Steering / pulling","amber","Pulling, wandering or a heavy wheel can mean steering, suspension or alignment.","Steering, suspension and alignment work.","brakes"),
]

CAP = {  # gallery captions + filter tags
 'g01':("The crew, out front","team"),
 'g16':("The crew under our sign","team"),
 'g03':("Engine bay open, new battery going in","shop"),
 'g15':("The alignment rack","shop"),
 'f07':("Lifts and the shop floor","shop"),
 'f08':("Hood up, diagnosis under way","shop"),
 'f01':("Tool carts and lifts","shop"),
 'g17':("The lobby: big windows, comfortable seats","lobby"),
 'g02':("Lobby seating while you wait","lobby"),
 'g08':("A classic flatbed pickup at the shop","classic"),
 'f10':("A classic 4x4 in for work","classic"),
 'g09':("A fresh set of wheels and tires","shop"),
 'g07':("The shop on NE 19th Dr","outside"),
 'f11':("Our service bays","outside"),
 'f03':("Out front, along the landscaping","outside"),
 'g10':("Our front door: hours and phone","outside"),
 'sign':("The roadside sign, since 1975","outside"),
}
