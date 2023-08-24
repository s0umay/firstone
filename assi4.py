class Matchs:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return team_matches

    def list_matches_by_location(self, location_name):
        location_matches = [match for match in self.matches if match.location == location_name]
        return location_matches

    def list_matches_by_timing(self, timing_type):
        timing_matches = [match for match in self.matches if match.timing == timing_type]
        return timing_matches

def main():
    table = FTable()

    # Adding matches to the table
    table.add_match(Matchs("Mumbai", "India", "Sri Lanka", "DAY"))
    table.add_match(Matchs("Delhi", "England", "Australia", "DAY-NIGHT"))
    table.add_match(Matchs("Chennai", "India", "South Africa", "DAY"))
    table.add_match(Matchs("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    table.add_match(Matchs("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    table.add_match(Matchs("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Select search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")
        c = int(input())

        if c == 1:
            team_name = input("Enter Team Name: ")
            matches = table.list_matches_by_team(team_name)
            for match in matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")

        elif c == 2:
            location_name = input("Enter Location Name: ")
            matches = table.list_matches_by_location(location_name)
            for match in matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")

        elif c == 3:
            timing_type = input("Enter Timing: ")
            matches = table.list_matches_by_timing(timing_type)
            for match in matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")

        elif c == 4:
            break

if __name__ == "__main__":
    main()
