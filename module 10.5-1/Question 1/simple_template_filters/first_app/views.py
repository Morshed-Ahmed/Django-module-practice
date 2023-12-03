from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    db = [
        {
            "title": "the science behind inspiration and how to design more of it into your life",
            "description":"If you’re like me, connecting with the creative muse has felt a bit strained the past few years. Finding inspiration can be hard in what feels like a nonstop stream of awful news, marked by climate disasters, humanitarian crises, a global pandemic, and what feels like the political upside-down. Staying inspired can be challenging as we experience a collective mental health dip¹ and work burnout is on the rise².",
            "time":datetime.strptime( "2023-12-03T10:30:00.000123","%Y-%m-%dT%H:%M:%S.%f")
        },
        {
            "title": "sometimes The Cracks Get Too Big to Hold a Friendship Together",
            "description":"We used to duck into the girls’ bathroom after class to refresh our lip gloss and eye liner (a newly acquired skill). Once, she’d tied my shoelaces to my desk right when the bell rang. I’d helplessly watched the class empty out while I tried to untie myself.",
            "time":datetime.strptime( "2023-12-02T10:30:00.000123","%Y-%m-%dT%H:%M:%S.%f")
        },
        {
            "title": "the Trouble With Teachability",
            "description":"Did you know that Warren Buffett advises against using a schedule? That way, he argues, you just do what’s most important at any given time. Buffet is as celebrated as Elon Musk when it comes to a certain kind of success, but I’d be willing to bet you’ve heard more about how to implement Musk’s five-minute interval schedule than Buffet’s advice to avoid scheduling entirely.",
            "time":datetime.strptime( "2023-12-01T10:30:00.000123","%Y-%m-%dT%H:%M:%S.%f")
        },
        {
            "title": "food Twin: Stress Testing the U.S. Food System",
            "description":"Today the Plotline, the food climate and data community organized by Earth Genome, is launching Food Twin, a proof of concept digital twin of the United States food system. Food Twin is based on a custom model, built in collaboration with food system expert Zia Mehrabi, that maps production of grown foods in the United States to where these foods are consumed. This model reveals a brittle and centralized food system that is at a high risk to be impacted by climate change economic shocks.",
            "time":datetime.strptime( "2023-10-02T10:30:00.000123","%Y-%m-%dT%H:%M:%S.%f")
        },
        {
            "title": "what I Wish We’d Done at the First Sign Mom Was Losing Her Memory",
            "description":"Then there was Tim’s funeral. Mom got lost returning to her hotel room to get a sweater. We found her wandering around outside the hotel. Concerning but anyone would be disoriented after burying their son.",
            "time":datetime.strptime( "2023-06-02T10:30:00.000123","%Y-%m-%dT%H:%M:%S.%f")
        },
        {
            "title": "the No Homework Policy",
            "description":"An early experience in making my own rules came when I entered high school. In the first weeks of my freshman year, I tried to do everything right. I did what I was told to do — and this included my homework. After lacrosse practice and my after-school job at a local supermarket, I got home around 8:00p.m. Then I had to eat some dinner, do homework, and go to sleep so I could wake up and do it all over again.",
            "time":datetime.strptime( "2023-12-03T11:30:00.000123","%Y-%m-%dT%H:%M:%S.%f")
        },
    ]
    return render(request,'Home.html',{"data":db})
