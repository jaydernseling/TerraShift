import earthaccess

# 1. Log in to NASA Earthdata and save credentials locally for future runs
auth = earthaccess.login(strategy="interactive", persist=True)

# 2. Search for NASA SMAP Soil Moisture data over Kota Samarahan - Asajaya
# bounding_box format: (west_lon, south_lat, east_lon, north_lat)
results = earthaccess.search_data(
    short_name="SPL4SMGP",
    bounding_box=(110.40, 1.35, 110.75, 1.65),
    temporal=("2026-10-01", "2026-10-05"),
    count=3
)

print(f"Success! Found {len(results)} NASA SMAP satellite files for Sarawak.")

# 3. Download the first file into a local folder named 'nasa_data'
if results:
    downloaded_files = earthaccess.download(results[:1], "./nasa_data")
    print("Downloaded file:", downloaded_files)