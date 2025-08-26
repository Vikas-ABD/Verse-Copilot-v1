# audio_player_device – UEFN Verse Device Documentation

## 🔹 Description
The `audio_player_device` lets you configure and play audio from a device location or directly from registered agents (players, creatures, or AI) in your Fortnite island. It is used for creating music, sound effects, ambience, and event-driven audio cues. Playback and targeting can be controlled dynamically, enabling rich interactive audio systems.

## 🧱 Imports Required
```verse
verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`  
  *Base class for creative devices and props.*
- `creative_device_base`  
  *Base class for `creative_device`.*
- `audio_player_device`

## 🧩 Core Methods
| Function Name | Signature / Description |
|---------------|--------------------------|
| `Enable()` | Enables the device. Allows triggering and allows `Play` to succeed. |
| `Disable()` | Disables this device. Prevents further triggers and stops any currently playing audio. |
| `Play()` | Starts playing audio from the device’s location. |
| `Play(Agent: agent)` | Starts playing audio for the specified agent (only if the device is set to be "Heard by Instigator"). |
| `Stop()` | Stops all currently playing audio from this device. |
| `Stop(Agent: agent)` | Stops audio for the specified agent (only if the device is set to be "Heard by Instigator"). |
| `Register(Agent: agent)` | Adds the agent as a target for audio playback when the device is activated. |
| `Unregister(Agent: agent)` | Removes the agent from the list of playback targets. |
| `UnregisterAll()` | Removes all previously registered agents as valid targets for audio playback. |
| `GetTransform()` | Returns the device’s world transform (location/rotation/scale). |
| `Hide()` | Hides the device mesh. |
| `Show()` | Shows the device mesh if previously hidden. |
| `MoveTo(Position, Rotation, Time)` | Moves device to specified position/rotation over specified seconds. Stops current animation. |
| `MoveTo(Transform, Time)` | Moves to transform over time; stops active animation. |
| `TeleportTo(Position, Rotation)` | Instantly teleports the device. |
| `TeleportTo(Transform)` | Instantly moves device to transform (position, rotation, and scale). |

## 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Audio Asset | The sound/music to play |
| Play on Start | Automatically start playback when the game begins |
| Looping | Play repeatedly |
| "Heard By" | Where audio is played: All, Team, Instigator |
| Volume, Pitch, Range | Sound properties and attenuation settings |
| Priority/Concurrency | For advanced audio management |
| Spatialization | 3D/ambient playback |

*Set these in the UEFN Details panel after placing the device.*

## 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Device to control audio playback
audio_controller := class(creative_device):

    @editable
    AudioDevice : audio_player_device = audio_player_device{}

    @editable
    PlayButton : button_device = button_device{}

    @editable
    StopButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to button interactions
        PlayButton.InteractedWithEvent.Subscribe(OnPlayAudio)
        StopButton.InteractedWithEvent.Subscribe(OnStopAudio)

    # Play audio from device location
    OnPlayAudio(Agent : agent) : void =
        AudioDevice.Play()

    # Stop audio playback
    OnStopAudio(Agent : agent) : void =
        AudioDevice.Stop()
```

## 🧠 Best Practices
- Assign the device as `@editable` and configure the correct audio and playback settings in the UEFN Details panel before runtime.
- Use `Register`/`Unregister` to dynamically include/exclude agents for agent-based sound cues.
- Use the “Heard By” setting to control whether sounds play for all players, by team, or just instigators.
- Use multiple `audio_player_device` instances for layered sound, music transitions, or spatial soundscapes.
- Check `IsValid` before using device if it might be destroyed during play (for `GetTransform` use).

## ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|------------------|--------------------|-------------|
| Not assigning @editable ref | Not setting device in Details panel | Assign device in Details and reference as `@editable` | Prevents nil/failed method calls |
| Unregistered agent for Play | Using `Play(Agent)` w/o registering agent | Register agent first, then call `Play(Agent)` | Required for agent-based playback |
| Device not enabled | Calling `Play()` after `Disable()` | Use `Enable()` before `Play()` as needed | Disabled device cannot play audio |

**Note:**
- `Play(Agent)` and `Stop(Agent)` only function when “Heard By Instigator” is enabled on the device.
- Typical audio flow: configure in Details panel → enable device → control playback via Verse or in-editor bindings.
- Use for music, interactive SFX, or dynamic agent-attached sounds for maximum flexibility in Fortnite experiences.

