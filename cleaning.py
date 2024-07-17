import pandas as pd
from youtubesearchpython import VideosSearch
from pytube import YouTube 


# Load the CSV file
file_path = './Conspiracy_Videos.csv'
videos_df = pd.read_csv(file_path)

# Function to check if a video exists
def check_video_exists(video_id):
    try:
        video_url='https://www.youtube.com/watch?v='+video_id
        
        video_search = YouTube(video_url)
        
        return (video_search.length > 0)
    except Exception as e:
        print(f"Error checking video ID {video_id}: {e}")
        return False

# Check each video and filter out those that don't exist
videos_df['Exists'] = videos_df['Video ID'].apply(check_video_exists)
videos_df_cleaned = videos_df[videos_df['Exists']].drop(columns=['Exists'])

# Save the cleaned dataframe to a new CSV file
output_file_path = './Cleaned_Conspiracy_Videos.csv'
videos_df_cleaned.to_csv(output_file_path, index=False)

print(f"Cleaned list saved to {output_file_path}")
