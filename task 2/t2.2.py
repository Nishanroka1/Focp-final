import sys

def analyze_cat_shelter_log(log_data):
  """
  Analyzes a cat shelter log file and prints a summary of the data.

  Args:
    log_data: A list of strings representing the log entries.

  Prints:
    A summary of the cat shelter log data, including the number of cat visits,
    the number of visits by other cats, the total time the cat spent in the shelter,
    the average visit length, the longest visit, and the shortest visit.
  """

  cat_visits = 0
  other_cats = 0
  total_cat_time = 0
  longest_visit = 0
  shortest_visit = 10000

  for entry in log_data:
    if entry == "END":
      break

    cat, start_time, end_time = entry.strip().split(",")
    start_time = int(start_time)
    end_time = int(end_time)

    visit_length = end_time - start_time

    if cat == "OURS":
      cat_visits += 1
      total_cat_time += visit_length
      longest_visit = max(longest_visit, visit_length)
      shortest_visit = min(shortest_visit, visit_length)
    else:
      other_cats += 1

  # Calculate total time in hours and minutes
  total_hours, total_minutes = divmod(total_cat_time, 60)

  # Print the analysis summary
  print("Log File Analysis")
  print("==================")
  print(f"Cat Visits: {cat_visits}")
  print(f"Other Cats: {other_cats}")
  print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes")
  print(f"Average Visit Length: {total_cat_time // cat_visits} Minutes")
  print(f"Longest Visit:        {longest_visit} Minutes")
  print(f"Shortest Visit:       {shortest_visit} Minutes")

# Example usage
# log_data = [
#   "OURS,600,630",
#   "THEIRS,700,701",
#   "OURS,842,900",
#   "THEIRS,1000,1001",
#   "THEIRS,1010,1011",
#   "END",
# ]

# analyze_cat_shelter_log(log_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py log_file.txt")
        sys.exit(1)

    log_file_path = sys.argv[1]

    try:
        with open(log_file_path, "r") as file:
            log_data = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        sys.exit(1)

    analyze_cat_shelter_log(log_data)