#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random


class SoccerTeam:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.fouls = random.randint(1, 10)
        self.passes_attempted = random.randint(80, 100)
        self.passes_completed = random.randint(60, 80)
        self.chances_created = random.randint(1, 15)
        self.tackles_completed = random.randint(40, 50)
        # stats are set to a random integer so that the stats are comparable to a real game
        # score is set to 0 and not a random integer so the score remains normal instead of being very high


team_list_2023 = ["Arsenal", "Liverpool", "Manchester City", "Aston Villa", "Tottenham", "Newcastle",
                  "Manchester United", "Brighton", "West Ham", "Chelsea", "Brentford", "Crystal Palace", "Wolves"
                  , "Fulham", "Nottingham Forest", "Bournemouth", "Luton Town", "Everton", "Burnley", "Sheffield United"]

team_A = SoccerTeam(random.choice(team_list_2023))
team_B = SoccerTeam(random.choice(team_list_2023))
while team_B.name == team_A.name:
    team_B = SoccerTeam(random.choice(team_list_2023))  # So that team B is never the same as team A

print(f"\nWelcome everybody! We have an exciting match up today between {team_A.name} and {team_B.name}.")


def simulate_soccer_game(team1, team2):
    simulate_half(team1, team2)

    print("\nHalftime Events:")
    halftime_event(team1, team2)

    simulate_half(team2, team1)

    print("\nOverall Stats:")
    display_stats(team1, team2)


def simulate_half(attacking_team, defending_team):
    print(f"\n{attacking_team.name} begins with the ball, and {defending_team.name} is defending.")

    simulate_event(attacking_team, defending_team)
    simulate_event(defending_team, attacking_team)
    simulate_event(attacking_team, defending_team)
    simulate_event(defending_team, attacking_team)


def simulate_event(attacking_team, defending_team):
    event_type = random.choice(["goal", "goal", "goal", "foul", "chance", "tackle"])
# goal is entered multiple times so that there are more chances for a goal, this leads to less ties

# important stats are shown using this function, hence the difference between the general stats displayed and the events
# during the halves

    if event_type == "goal":
        attacking_team.score += 1
        print(f"⚽ GOAL! {attacking_team.name} scores!")

    elif event_type == "foul":
        attacking_team.fouls += 1
        print(f"🔶 FOUL! {attacking_team.name} commits a harsh foul on {defending_team.name}.")

    elif event_type == "chance":
        attacking_team.chances_created += 1
        print(f"🎯 CHANCE! {attacking_team.name} creates a scoring chance, but fails to finish.")

    elif event_type == "tackle":
        attacking_team.tackles_completed += 1
        print(f"👟 TACKLE! {attacking_team.name} completes an important tackle.")


def halftime_event(team1, team2):
    winning_team = team1 if team1.score > team2.score else team2
    losing_team = team2 if team1.score > team2.score else team1
    print(f"The score is currently {losing_team.score} - {winning_team.score}, favoring {winning_team.name}.\n"
          f"{losing_team.name} rethinks their strategy for the next half.\n"
          f"{winning_team.name} continues their current strategy.")


def display_stats(team1, team2):
    total_passes_attempted = team1.passes_attempted + team2.passes_attempted
    total_passes_completed = team1.passes_completed + team2.passes_completed

    possession_team1 = (team1.passes_completed / total_passes_completed) * 100
    possession_team2 = (team2.passes_completed / total_passes_completed) * 100

    print(f"{team1.name} {team1.score} - {team2.score} {team2.name}")
    print(f"{team1.name} Fouls: {team1.fouls}, {team2.name} fouls: {team2.fouls}")
    print(f"{team1.name} Possession: {possession_team1:.2f}%, {team2.name} possession: {possession_team2:.2f}%")
    print(f"{team1.name} Chances Created: {team1.chances_created}")
    print(f"{team2.name} Chances Created: {team2.chances_created}")
    print(f"{team1.name} Important Tackles: {team1.tackles_completed}")
    print(f"{team2.name} Important Tackles: {team2.tackles_completed}")


simulate_soccer_game(team_A, team_B)


# In[ ]:




