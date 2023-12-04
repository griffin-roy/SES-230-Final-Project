#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random


class SoccerTeam:
    def __init__(self, name, win_probability):
        self.name = name
        self.score = 0
        self.fouls = random.randint(1, 10)
        self.passes_attempted = random.randint(80, 100)
        self.passes_completed = random.randint(60, 80)
        self.chances_created = random.randint(1, 15)
        self.tackles_completed = random.randint(25, 50)
        self.win_probability = win_probability


team_A = SoccerTeam("Manchester City", win_probability=74)
team_B = SoccerTeam("Southampton", win_probability=16)
# probabilities calculated by looking at their 2022/23 season wins / games played

print(f"\nWelcome everybody! We have an exciting match up today between {team_A.name} and {team_B.name}.")


def simulate_soccer_game(team1, team2):
    simulate_half(team1, team2)

    print("\nHalftime:")
    halftime_event(team1, team2)

    simulate_half(team2, team1)

    print("\nOverall Stats:")
    display_stats(team1, team2)


def simulate_half(attacking_team, defending_team):
    print(f"\n{attacking_team.name} is attacking, and {defending_team.name} is defending.")

    simulate_event(attacking_team, defending_team)
    simulate_event(attacking_team, defending_team)
    simulate_event(attacking_team, defending_team)
    simulate_event(attacking_team, defending_team)


def simulate_event(attacking_team, defending_team):
    event_type = random.choice(["goal", "goal", "goal", "foul", "chance", "tackle"])
# goal is entered multiple times so that there are more chances for a goal, this leads to less ties

# Some of the major events are shown in the output, not all of them,
    # hence the difference between the events and the end stats

    win_factor = attacking_team.win_probability / (attacking_team.win_probability + defending_team.win_probability)
    if random.random() < win_factor:
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
    print(f"The score is currently {losing_team.score} - {winning_team.score}, with the flow of the game favoring {winning_team.name}.\n"
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
    print(f"{team1.name} Chances Created: {team1.chances_created}, {team2.name} Chances Created: {team2.chances_created}")
    print(f"{team1.name} Important Tackles: {team1.tackles_completed}, {team2.name} Important Tackles: {team2.tackles_completed}")


def simulate_multiple_games(team_A, team_B, num_games):
    wins_team_A = 0
    wins_team_B = 0

    for i in range(num_games):
        current_team_A = SoccerTeam(team_A.name, win_probability=74)
        current_team_B = SoccerTeam(team_B.name, win_probability=16)

        simulate_soccer_game(current_team_A, current_team_B)

        if current_team_A.score > current_team_B.score:
            wins_team_A += 1
        elif current_team_B.score > current_team_A.score:
            wins_team_B += 1

    print(f"\nResults after {num_games} games:")
    print(f"{team_A.name} wins: {wins_team_A}")
    print(f"{team_B.name} wins: {wins_team_B}")


simulate_multiple_games(team_A, team_B, num_games=10)
# doing more games may not be good for the computer, so the code can just be run 10 times to get to 100 games if needed


# In[ ]:




