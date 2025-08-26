📘 video_player_device – UEFN Verse Device Documentation

🔹 Description
The video_player_device allows you to display curated video streams on in-game screens or the player HUD in Fortnite. Use this device to showcase trailers, tutorials, minigame intros, or other video content directly in your experience. It supports enabling/disabling, fullscreen and picture-in-picture modes, restarting, seeking, managing control, and reacting to stream events.

🧱 Verse Using Statement
```
verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- video_player_device

🧩 Data Members (Events)
| Event Name          | Type              | Description                                                        |
|---------------------|-------------------|--------------------------------------------------------------------|
| StreamStartedEvent  | listenable(agent) | Fires when this device becomes the active streaming device for agent. |

🛠️ Functions & Methods
| Name/Method              | Description                                                        |
|--------------------------|--------------------------------------------------------------------|
| Enable()                 | Turns video ON.                                                    |
| Disable()                | Turns video OFF.                                                   |
| EnableCollision()        | Enables collision checks.                                          |
| DisableCollision()       | Disables collision checks.                                         |
| EnterFullScreen(Agent)   | Makes the video fullscreen for the agent.                          |
| ExitFullScreen(Agent)    | Exits fullscreen mode for the agent.                               |
| HidePIP(Agent)           | Hides picture-in-picture mode for the agent.                       |
| MakePIPDefaultSize(Agent)| Resets PIP video to default size.                                  |
| MakePIPFullScreen(Agent) | Makes PIP video fullscreen.                                        |
| EndForAll()              | Stops all devices of this type on the island.                      |
| Restart()                | Restarts the video stream.                                         |
| Seek()                   | Seeks to a triggered point in the stream.                          |
| TakeControl()            | Forces playback control to this device with audio.                 |
| ReleaseControl()         | Releases control back to priority stream.                          |

🎛 Configuration Options (Details Panel)
- Video Source: Choose from curated sources.
- Show On HUD/In-World: Select display location.
- Autoplay: Enable autoplay.
- Show Player Controls: Allow player UI controls.
- Loop Video: Loop playback.
- Audio Settings: Volume, mute, output config.
- Collision: Enable/disable interaction.

🧰 Verse Usage Example
```
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

video_player_example := class(creative_device):

    @editable
    VideoPlayer : video_player_device = video_player_device{}
    
    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    FullscreenButton : button_device = button_device{}

    @editable
    PiPButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        VideoPlayer.StreamStartedEvent.Subscribe(OnStreamStarted)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        FullscreenButton.InteractedWithEvent.Subscribe(OnFullscreenPressed)
        PiPButton.InteractedWithEvent.Subscribe(OnPiPPressed)

    OnStreamStarted(Agent : agent) : void =
        Print("Video stream started!")

    OnEnablePressed(Agent : agent) : void =
        VideoPlayer.Enable()
        Print("Video player enabled!")

    OnDisablePressed(Agent : agent) : void =
        VideoPlayer.Disable()
        Print("Video player disabled!")

    OnFullscreenPressed(Agent : agent) : void =
        Print("Fullscreen mode is not supported by video_player_device.")

    OnPiPPressed(Agent : agent) : void =
        Print("Picture-in-picture mode is not supported by video_player_device.")

    RestartVideo() : void =
        VideoPlayer.Restart()
        Print("Video restarted!")

    SeekVideo() : void =
        VideoPlayer.Seek()
        Print("Video seeked to beginning!")

    TakeControl() : void =
        VideoPlayer.TakeControl()
        Print("Control taken for video player!")

    ReleaseControl() : void =
        VideoPlayer.ReleaseControl()
        Print("Control released for video player!")
```

🛠 How it works in UEFN
1. **Place Devices in Level**
   - Add a video_player_device and a screen from the Devices tab or Galleries.
   - Add control button_devices for interaction.

2. **Configure Device in Details Panel**
   - Assign video source, HUD or screen display, autoplay, loop, controls, and collision.

3. **Add & Build the Verse Script**
   - Create a Verse file (e.g., `video_player_example.verse`).
   - Paste the script and build using `CTRL+SHIFT+B` until "Build Succeeded".

4. **Place & Reference Devices**
   - Drag the script class into the world.
   - In the Details panel, assign references for VideoPlayer and buttons.

5. **Test in Play Session**
   - Interact with buttons in-game to enable, disable, or simulate modes.

🧠 Best Practices
- Use `.Enable()` and `.Disable()` for event-driven playback.
- Handle `StreamStartedEvent` for synchronized gameplay actions.
- Combine with HUD and UI logic for immersive experience.
- Adjust collision and display settings for intended gameplay effects.

❌ Common Mistakes & Fixes
| Issue                    | ❌ Wrong Usage                             | ✅ Correct Usage                              | Explanation                                |
|-------------------------|-------------------------------------------|----------------------------------------------|--------------------------------------------|
| Video doesn't play      | Device not enabled / autoplay off         | Call `.Enable()` or enable Autoplay          | Must trigger playback                      |
| Fullscreen/PiP fails    | Missing agent in method call              | Use `EnterFullScreen(agent)` etc.            | Agent context required                     |
| Device unresponsive     | Device references not assigned in Verse   | Assign in Details panel                      | Devices won’t respond otherwise            |
| Video not visible       | Unapproved or missing video source        | Select from curated list in Details panel    | Only approved videos are supported         |

📌 Note:
- Only curated videos are supported, not arbitrary uploads.
- Use per-agent methods for HUD/video control.
- Integrate with gameplay logic for advanced use cases like tutorials or cutscenes.

