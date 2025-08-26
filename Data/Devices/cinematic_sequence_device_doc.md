# UEFN Verse Device Documentation: `cinematic_sequence_device`

## 📙 Description

The `cinematic_sequence_device` in **Unreal Editor for Fortnite (UEFN)** allows creators to play custom Level Sequences in-game. These sequences can contain:

- Complex animations
- Object movements
- Camera choreography
- Audio

This device is ideal for cutscenes, cinematics, or scripted gameplay moments. It supports play control (Play, Pause, Stop, Reverse, etc.), querying current playback time or frame, and subscribing to events using Verse or other creative devices.

## 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `cinematic_sequence_device`

---

## 🛠️ Key Methods & Functions

| Method                      | Overload                | Description                                      |
| --------------------------- | ----------------------- | ------------------------------------------------ |
| `Play()`                    | `Play(agent)`           | Start/resume sequence playback                   |
| `Pause()`                   | `Pause(agent)`          | Pause sequence playback                          |
| `Stop()`                    | `Stop(agent)`           | Stop & reset sequence (to beginning)             |
| `PlayReverse()`             | `PlayReverse(agent)`    | Play sequence in reverse                         |
| `TogglePause()`             | `TogglePause(agent)`    | Toggle play/pause state                          |
| `GoToEndAndStop()`          | `GoToEndAndStop(agent)` | Jump to end of sequence and stop                 |
| `SetPlaybackFrame(f)`       |                         | Set sequence playback to frame number `f`        |
| `SetPlaybackTime(s)`        |                         | Set sequence playback to time `s` in seconds     |
| `SetPlayRate(f)`            |                         | Set playback speed                               |
| `GetPlaybackFrame()`        |                         | Get current playback frame                       |
| `GetPlaybackTime()`         |                         | Get current playback time (in seconds)           |
| `GetPlayRate()`             |                         | Get playback rate                                |
| `GetTransform()`            |                         | Get world transform of the device                |
| `MoveTo()` / `TeleportTo()` |                         | Move, animate, or teleport device in world space |

---

## 🧹 Events (Data Members)

| Name           | Type                  | Fires When                                             |
| -------------- | --------------------- | ------------------------------------------------------ |
| `StoppedEvent` | `listenable(tuple())` | When sequence has stopped (ended/stopped/pause-to-end) |

---

## 💻 Device Configuration (Details Panel)

| Option                  | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| Sequence                | Assign a Level Sequence asset                              |
| Loop Playback           | Sequence repeats until manually stopped                    |
| Finish Completion State | Restore or keep object states at sequence end              |
| Auto Play               | Sequence plays on game start (with phase options)          |
| Visibility              | Who can see the sequence (Everyone, Instigator Only, etc.) |
| Networking Relevance    | Set playback relevance (always relevant or distance-based) |

---

## 🧠 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

cinematic_sequence_example := class(creative_device):

    @editable
    SequenceDevice : cinematic_sequence_device = cinematic_sequence_device{}

    @editable
    PlayButton : button_device = button_device{}

    @editable
    PauseButton : button_device = button_device{}

    @editable
    StopButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SequenceDevice.StoppedEvent.Subscribe(OnSequenceStopped)
        PlayButton.InteractedWithEvent.Subscribe(OnPlayPressed)
        PauseButton.InteractedWithEvent.Subscribe(OnPausePressed)
        StopButton.InteractedWithEvent.Subscribe(OnStopPressed)

    OnSequenceStopped() : void =
        Print("Cinematic sequence stopped!")

    OnPlayPressed(Agent : agent) : void =
        SequenceDevice.Play()
        Print("Cinematic sequence playing!")

    OnPausePressed(Agent : agent) : void =
        SequenceDevice.Pause()
        Print("Cinematic sequence paused!")

    OnStopPressed(Agent : agent) : void =
        SequenceDevice.Stop()
        Print("Cinematic sequence stopped!")
```

### Explanation

- **SequenceDevice**: Reference to the cinematic sequence placed in the level.
- **Play/Pause/Stop Buttons**: Button devices linked to control the sequence.
- **Event Subscriptions**: Connect button events and sequence events to custom logic.

---

## 📆 How to Use in UEFN

1. **Create/Import Your Sequence**

   - Right-click Content Browser > Cinematic > Level Sequence.

2. **Place the Cinematic Sequence Device**

   - Content Browser > Devices > Cinematic Sequence > Drag to your level.

3. **Configure the Device**

   - Assign Level Sequence, set options (loop, auto play, visibility).

4. **Create a Verse Script**

   - Open **Verse Explorer**.
   - Create a new Verse file (e.g., `cinematic_sequence_example.verse`).
   - Paste example code and save.
   - Build code (`Ctrl+Shift+B`) until "Build Succeeded."
   - Drag Verse device into world and assign fields.

5. **Playtest**

   - Use buttons to control sequence.
   - Output Log shows playback messages.
   - Connect `StoppedEvent` to trigger gameplay logic.

---

## 🧠 Best Practices

- Use `StoppedEvent` to:
  - Enable gameplay controls
  - Complete objectives
  - Trigger follow-up sequences
- Adjust visibility, auto play, and relevance for multiplayer.
- Use Verse to:
  - Move/animate cameras or controllers
  - Spawn or activate objects
  - Lock input or UI during cutscenes

---

## ❌ Common Issues & Fixes

| Issue                   | Reason                               | Solution                                             |
| ----------------------- | ------------------------------------ | ---------------------------------------------------- |
| Sequence doesn’t play   | Sequence missing, device not enabled | Assign sequence in Details and enable device         |
| Only some players see   | Visibility set to Instigator Only    | Set to "Everyone" or handle in Verse with agent      |
| Out-of-sync multiplayer | Relevance settings                   | Set to "Always Relevant" and test device performance |

---

> ⚠️ **Note:**
>
> - Use the Level Sequence Editor for timeline events.
> - Control Rig can be used for advanced animation control.
> - Combine Verse with trigger wiring for full cinematic control, transitions, and rewards.

