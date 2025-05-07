from django import forms

IPL_TEAMS = [
    ('RCB', 'RCB'),
    ('GT', 'GT'),
    ('MI', 'MI'),
    ('SRH', 'SRH'),
    ('KKR', 'KKR'),
    ('LSG', 'LSG'),
    ('DC', 'DC'),
    ('CSK', 'CSK'),
    ('PBKS', 'PBKS'),
    ('RR', 'RR'),
    ('KXIP', 'KXIP'),
    ('RPS', 'RPS'),
    ('GL', 'GL'),
    ('PWI', 'PWI'),
    ('Kochi', 'Kochi')
]


class MatchForm(forms.Form):
    team1 = forms.ChoiceField(label="Team 1", choices=IPL_TEAMS)
    team2 = forms.ChoiceField(label="Team 2", choices=IPL_TEAMS)
    team1_score = forms.IntegerField(label="Team 1 Score")

VENUE_CHOICES = [
    ('Arun Jaitley Stadium, Delhi', 'Arun Jaitley Stadium, Delhi'),
    ('Barabati Stadium, Cuttack', 'Barabati Stadium, Cuttack'),
    ('Barsapara Cricket Stadium, Guwahati', 'Barsapara Cricket Stadium, Guwahati'),
    ('Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow', 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow'),
    ('Brabourne Stadium, Mumbai', 'Brabourne Stadium, Mumbai'),
    ('Buffalo Park, East London', 'Buffalo Park, East London'),
    ('Diamond Oval, Kimberley', 'Diamond Oval, Kimberley'),
    ('Dr DY Patil Sports Academy, Mumbai', 'Dr DY Patil Sports Academy, Mumbai'),
    ('Dr DY Patil Sports Academy, Navi Mumbai', 'Dr DY Patil Sports Academy, Navi Mumbai'),
    ('Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam'),
    ('Dubai International Cricket Stadium', 'Dubai International Cricket Stadium'),
    ('Eden Gardens, Kolkata', 'Eden Gardens, Kolkata'),
    ('Green Park, Kanpur', 'Green Park, Kanpur'),
    ('Himachal Pradesh Cricket Association Stadium, Dharamsala', 'Himachal Pradesh Cricket Association Stadium, Dharamsala'),
    ('Holkar Cricket Stadium, Indore', 'Holkar Cricket Stadium, Indore'),
    ('JSCA International Stadium Complex, Ranchi', 'JSCA International Stadium Complex, Ranchi'),
    ('Kingsmead, Durban', 'Kingsmead, Durban'),
    ('M.Chinnaswamy Stadium, Bengaluru', 'M.Chinnaswamy Stadium, Bengaluru'),
    ('MA Chidambaram Stadium, Chepauk, Chennai', 'MA Chidambaram Stadium, Chepauk, Chennai'),
    ('Maharashtra Cricket Association Stadium, Pune', 'Maharashtra Cricket Association Stadium, Pune'),
    ('Mangaung Oval, Bloemfontein', 'Mangaung Oval, Bloemfontein'),
    ('Narendra Modi Stadium, Motera, Ahmedabad', 'Narendra Modi Stadium, Motera, Ahmedabad'),
    ('Nehru Stadium, Kochi', 'Nehru Stadium, Kochi'),
    ('Newlands, Cape Town', 'Newlands, Cape Town'),
    ('Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh', 'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh'),
    ('Rajiv Gandhi International Stadium, Uppal, Hyderabad', 'Rajiv Gandhi International Stadium, Uppal, Hyderabad'),
    ('Sardar Patel (Gujarat) Stadium, Motera, Ahmedabad', 'Sardar Patel (Gujarat) Stadium, Motera, Ahmedabad'),
    ('Saurashtra Cricket Association Stadium, Rajkot', 'Saurashtra Cricket Association Stadium, Rajkot'),
    ('Sawai Mansingh Stadium, Jaipur', 'Sawai Mansingh Stadium, Jaipur'),
    ('Shaheed Veer Narayan Singh International Stadium, Raipur', 'Shaheed Veer Narayan Singh International Stadium, Raipur'),
    ('Sharjah Cricket Stadium', 'Sharjah Cricket Stadium'),
    ('Sheikh Zayed Stadium, Abu Dhabi', 'Sheikh Zayed Stadium, Abu Dhabi'),
    ("St George's Park, Port Elizabeth", "St George's Park, Port Elizabeth"),
    ('SuperSport Park, Centurion', 'SuperSport Park, Centurion'),
    ('The Wanderers Stadium, Johannesburg', 'The Wanderers Stadium, Johannesburg'),
    ('Vidarbha Cricket Association Stadium, Jamtha, Nagpur', 'Vidarbha Cricket Association Stadium, Jamtha, Nagpur'),
    ('Wankhede Stadium, Mumbai', 'Wankhede Stadium, Mumbai'),
]

class ScoreInputForm(forms.Form):
    home_team = forms.ChoiceField(label="Home Team", choices=IPL_TEAMS)
    away_team = forms.ChoiceField(label="Away Team", choices=IPL_TEAMS)
    toss_won = forms.ChoiceField(label="Toss Won By", choices=IPL_TEAMS)
    decision = forms.ChoiceField(label="Decision", choices=[('BAT FIRST', 'Bat First'), ('BOWL FIRST', 'Bowl First')])
    venue_name = forms.ChoiceField(label="Venue", choices=VENUE_CHOICES)