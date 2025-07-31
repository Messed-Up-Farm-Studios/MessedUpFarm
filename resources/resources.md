## Resources

### Downloading Project Resources

To get the media files and resources for this project, follow these steps:

1. **Access the Google Drive folder**: 
   - Visit: https://drive.google.com/drive/folders/1zO-5BSK5gO4JAz51-WyhKbAoKTO2ZJou?usp=sharing
   - You may need to sign in to your Google account

2. **Download the resources**:
   - Select all files in the folder
   - Right-click and choose "Download" or use the download button
   - Alternatively, you can download individual files as needed

3. **Extract and organize**:
   - Extract the downloaded ZIP file (if applicable)
   - Place the media files in the appropriate directories in your project
   - Ensure the file paths match what your code expects

### Resource Types

The Google Drive folder contains various media files including:
- Sprite images (PNG format recommended)
- Sound effects and music
- Background images
- UI elements and icons

### File Organization

After downloading, organize your resources as follows:

### Usage in Code

Once downloaded, you can reference these resources in your Arcade code:

```python
# Example sprite loading
player_sprite = arcade.Sprite("resources/sprites/player.png", scale=1.0)
```

### Troubleshooting

- If you can't access the Google Drive folder, ensure you're signed in to Google
- If files don't load, check that the file paths in your code match the actual file locations
- Make sure image files are in supported formats (PNG, JPG, etc.)
- For sound files, ensure they're in supported formats (WAV, MP3, etc.)
