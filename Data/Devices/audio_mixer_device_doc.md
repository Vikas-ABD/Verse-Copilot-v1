# audio_mixer_device – UEFN Verse Device Documentation

## 🖊 Description
The `audio_mixer_device` is used to manage sound buses and control bus mixes in your Fortnite island. With this device, you can dynamically adjust the volume or properties of groups of sounds—called "control buses"—such as Music, SFX, Footsteps, Weapons, Vehicles, and more. Control can be activated or deactivated on demand, and you can specify which players or teams are affected.

## 🧱 Imports Required
```verse
verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`  
  Base class for creative devices and props.
- `creative_device_base`  
  Base class for creative_device.
- `audio_mixer_device`

## 🧹 Core Methods
| Function Name        | Signature / Description                                           |
|----------------------|------------------------------------------------------------------|
| ActivateMix()        | Activates (applies) the control bus mix on this device.          |
| DeactivateMix()      | Deactivates (removes) the control bus mix on this device.        |
| Register(Agent)      | Adds Agent to the list of players affected by the mix.           |
| Unregister(Agent)    | Removes Agent from the list.                                     |
| UnregisterAll()      | Removes all agents; mix applies to none except default.          |
| GetTransform()       | Returns the device’s transform in the world (cm units).           |
| MoveTo()/TeleportTo()| Move or teleport device in world (not usually needed).           |

## 🎚 Configuration Options (Details Panel)
| Option                 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Bus                    | Choose which group of sounds to control (Music, SFX, Ambience, etc.).      |
| Fader Value            | Sets volume multiplier (default = 1.0 = 100% volume).                       |
| Can Be Heard By        | Determines who is affected (None, Registered, Non-Registered, All).        |
| Activate at Game Start | Whether mix is enabled when the game starts.                               |
| Mix                    | (Advanced) Select a control bus mix asset for custom setups.               |
| Attack/Release Time    | How quickly the mix fades in/out when activated/deactivated.               |

## 🎧 Default Control Buses Table
| Control Bus Name   | Description                            |
|--------------------|----------------------------------------|
| Music              | All music/emote music                  |
| SFX                | All sound effects (general)            |
| Ambience           | Environmental & ambient sounds         |
| Explosions         | Explosion sounds                       |
| Footsteps          | Character footsteps                    |
| Gadgets            | Creative device/gadget sounds          |
| Impacts            | Impact sounds                          |
| Vehicles           | All vehicle sounds except engines      |
| Vehicle Engines    | Vehicle engine sounds                  |
| Weapons            | Weapon fire, reload etc.               |

## 🪰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

audio_mixer_controller := class(creative_device):

    @editable
    AudioMixer : audio_mixer_device = audio_mixer_device{}
    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to button interactions
        EnableButton.InteractedWithEvent.Subscribe(OnEnableMixer)
        DisableButton.InteractedWithEvent.Subscribe(OnDisableMixer)

    # Enable the audio mixer
    OnEnableMixer(Agent : agent) : void =
        AudioMixer.ActivateMix()
        Print("Audio mixer enabled")

    # Disable the audio mixer
    OnDisableMixer(Agent : agent) : void =
        AudioMixer.DeactivateMix()
        Print("Audio mixer disabled")
```

## 🧠 Best Practices
- In the Details panel, choose the appropriate Bus and Fader Value for your use case.
- Use Verse or direct function bindings to activate/deactivate the mix for clear transitions.
- Register/unregister agents to limit the audio effect to certain players or events.
- Avoid stacking multiple mixes unless a complex multi-bus setup is needed.
- For per-agent mixes, register individual agents and handle transitions in Verse.

## ❌ Incorrect Usage Examples and How to Fix
| Issue                            | ❌ Wrong Example                    | ✅ Correct Example                | Explanation                                     |
|----------------------------------|---------------------------------------|-------------------------------------|-------------------------------------------------|
| Not assigning device reference   | Calling methods on unreferenced device| Assign device in Details panel     | Prevents nil/error access in Verse              |
| Not activating mix               | Only setting Fader Value              | Always call ActivateMix()          | Changes go into effect only upon activation     |
| Using DeactivateMix improperly  | DeactivateMix() before ActivateMix()  | Always activate first              | No effect if mix not active                     |

## ⚠️ Notes
- Effects apply only to the chosen bus; for multi-group control, place one device per bus.
- XP/Analytics are not affected or detected by this device.
- Always save, build, and assign all device references after editing in UEFN or Verse.

