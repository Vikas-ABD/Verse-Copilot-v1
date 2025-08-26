## shooting\_range\_target\_track\_device – UEFN Verse Device Documentation

### 🔹 Description

The `shooting_range_target_track_device` provides a moving target that travels along a track and can be popped up or down to present shooting challenges for players. The track and its target are highly configurable: you can control position, speed, activation, reaction to being hit/eliminated, and how the device interacts with scoring, events, and gameplay logic. The device's events and actions can be fully managed in Verse or with in-editor settings.

### 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `shooting_range_target_track_device`

### 🧹 Events (Data Members)

| Event Name       | Type         | Description                                              |
| ---------------- | ------------ | -------------------------------------------------------- |
| BullseyeHitEvent | listenable() | Triggered when the moving target is hit in the bullseye. |
| HitEvent         | listenable() | Triggered whenever the moving target is hit.             |
| KnockdownEvent   | listenable() | Triggered if the moving target is knocked down.          |
| HopUpEvent       | listenable() | Triggered when target hops up slightly.                  |
| HopDownEvent     | listenable() | Triggered when target hops down slightly.                |
| PopUpEvent       | listenable() | When target rises from flat to standing (active).        |
| PopDownEvent     | listenable() | When target drops from standing to flat (inactive).      |

### 🛠️ Functions & Methods

| Function Name          | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| Enable()               | Enables the device and makes it responsive to triggers. |
| Disable()              | Disables the device.                                    |
| Reset()                | Resets the track/target to original configuration.      |
| PopUp()                | Pops target into standing position.                     |
| PopDown()              | Pops target down (inactive).                            |
| HopUp()                | Moves upright target slightly up.                       |
| HopDown()              | Moves upright target slightly down.                     |
| EnableTrackMovement()  | Allows target to move along the track.                  |
| DisableTrackMovement() | Freezes all movement along the track.                   |
| ActivateTrack()        | Starts movement along the track.                        |
| DeactivateTrack()      | Stops all movement on the track.                        |
| MoveToStart()          | Sends moving target to the start of the track.          |
| MoveToEnd()            | Sends moving target to the end of the track.            |
| GetTransform()         | Returns the current transform of the moving target.     |
| MoveTo()/TeleportTo()  | Moves/teleports the target to a specific location.      |

### 🎠 Configuration Options (Details Panel)

| Option                   | Description                                        |
| ------------------------ | -------------------------------------------------- |
| Track Length             | The distance the target moves (in tiles).          |
| Speed                    | How quickly the target moves along the track.      |
| Continuous Movement      | Whether it repeats motion or stops at track ends.  |
| Target Type              | Visual appearance/style of the target.             |
| Active at Game Start     | Is target moving at round start?                   |
| Scoring/Bullseye Options | Points for regular/bullseye hits, score team, etc. |
| Movement by Proximity    | Only moves when player is near, if enabled.        |
|                          |                                                    |

| *(many more)* | See UEFN Details for all options. |
| ------------- | --------------------------------- |

### 🧰 Verse Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

shooting_range_track_example := class(creative_device):

    @editable
    TargetTrack : shooting_range_target_track_device = shooting_range_target_track_device{}

    @editable
    MoveToStartButton : button_device = button_device{}

    @editable
    MoveToEndButton : button_device = button_device{}

    @editable
    PopUpButton : button_device = button_device{}

    @editable
    PopDownButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        TargetTrack.BullseyeHitEvent.Subscribe(OnBullseyeHit)
        TargetTrack.HitEvent.Subscribe(OnTargetHit)
        TargetTrack.KnockdownEvent.Subscribe(OnTargetKnockdown)

        MoveToStartButton.InteractedWithEvent.Subscribe(OnMoveToStart)
        MoveToEndButton.InteractedWithEvent.Subscribe(OnMoveToEnd)
        PopUpButton.InteractedWithEvent.Subscribe(OnPopUp)
        PopDownButton.InteractedWithEvent.Subscribe(OnPopDown)

        TargetTrack.EnableTrackMovement()
        TargetTrack.PopUp()

    OnBullseyeHit() : void =
        Print("Bullseye hit on moving target!")

    OnTargetHit() : void =
        Print("Target was hit!")

    OnTargetKnockdown() : void =
        Print("Moving target knocked down!")

    OnMoveToStart(Agent : agent) : void =
        TargetTrack.MoveToStart()
        Print("Target moving to start of track")

    OnMoveToEnd(Agent : agent) : void =
        TargetTrack.MoveToEnd()
        Print("Target moving to end of track")

    OnPopUp(Agent : agent) : void =
        TargetTrack.PopUp()
        Print("Target popped up")

    OnPopDown(Agent : agent) : void =
        TargetTrack.PopDown()
        Print("Target popped down")
```

### 📆 How to Use in UEFN

**1. Place Device & Controls**

- Drag a `shooting_range_target_track_device` into the world.
- Place `button_devices` for controls: Move to Start, Move to End, Pop Up, Pop Down.

**2. Create Your Verse File**

- In UEFN, go to **Verse → Verse Explorer**.
- Right-click a folder → **Create New Verse File** (e.g., `shooting_range_track_example.verse`).
- Choose **Create Empty**, paste in the sample code, and save.

**3. Build and Assign**

- Click **Verse → Build Verse Code** (`Ctrl+Shift+B`) until “Build Succeeded”.
- In Content Browser, drag your Verse device into the world.
- In Details, assign:
  - `TargetTrack` → your placed track device
  - Each `Button` → its respective button

**4. Configure Device Settings**

- Set all options (speed, score, visual style, etc.) in Details for the track device.

**5. Test and Play**

- Use the buttons and shoot at the moving target to ensure events fire and controls work.

### 🧠 Tips

- Use the device’s events in Verse to log hits, increase score, or add advanced feedback.
- Experiment with **Continuous Movement** and **Proximity** options for different gameplay styles.
- Combine with score devices for minigames or competitions.

### ❌ Common Issues & Solutions

| Issue               | Cause                      | Solution                         |
| ------------------- | -------------------------- | -------------------------------- |
| Target doesn’t move | Track movement not enabled | Call `.EnableTrackMovement()`    |
| No events triggered | Event not subscribed       | Use `.Subscribe()` in Verse code |
| Buttons do nothing  | References not set         | Assign all references in Details |

> **Note:**
>
> - For a stationary pop-up target, use `shooting_range_target_device` instead.
> - All device state changes (enable, move, pop) can be controlled in real-time with Verse.

