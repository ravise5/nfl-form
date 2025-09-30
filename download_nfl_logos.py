#!/usr/bin/env python3
"""
Script to download NFL team SVG logos from acrisurestadium.com
"""

import os
import requests
from urllib.parse import urljoin
import time

# Base URL for NFL team logos
BASE_URL = "https://acrisurestadium.com/wp-content/uploads/gbl/nfl-team-logos/"

# NFL teams with their URL-friendly names
NFL_TEAMS = [
    "arizona-cardinals",
    "atlanta-falcons", 
    "baltimore-ravens",
    "buffalo-bills",
    "carolina-panthers",
    "chicago-bears",
    "cincinnati-bengals",
    "cleveland-browns",
    "dallas-cowboys",
    "denver-broncos",
    "detroit-lions",
    "green-bay-packers",
    "houston-texans",
    "indianapolis-colts",
    "jacksonville-jaguars",
    "kansas-city-chiefs",
    "las-vegas-raiders",
    "los-angeles-chargers",
    "los-angeles-rams",
    "miami-dolphins",
    "minnesota-vikings",
    "new-england-patriots",
    "new-orleans-saints",
    "new-york-giants",
    "new-york-jets",
    "philadelphia-eagles",
    "pittsburgh-steelers",
    "san-francisco-49ers",
    "seattle-seahawks",
    "tampa-bay-buccaneers",
    "tennessee-titans",
    "washington-commanders"
]

def create_output_directory():
    """Create output directory for logos if it doesn't exist"""
    output_dir = "nfl_logos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    return output_dir

def download_logo(team_name, output_dir):
    """Download SVG logo for a specific team"""
    filename = f"{team_name}-logo.svg"
    url = urljoin(BASE_URL, filename)
    
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Successfully downloaded: {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    """Main function to download all NFL team logos"""
    print("NFL Team Logo Downloader")
    print("=" * 40)
    
    # Create output directory
    output_dir = create_output_directory()
    
    # Download logos
    successful_downloads = 0
    failed_downloads = 0
    
    for team in NFL_TEAMS:
        if download_logo(team, output_dir):
            successful_downloads += 1
        else:
            failed_downloads += 1
        
        # Small delay to be respectful to the server
        time.sleep(0.5)
    
    # Summary
    print("\n" + "=" * 40)
    print(f"Download Summary:")
    print(f"✓ Successful: {successful_downloads}")
    print(f"✗ Failed: {failed_downloads}")
    print(f"📁 Logos saved to: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    main()
