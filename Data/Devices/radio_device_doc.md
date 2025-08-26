**radio\_device – UEFN Verse Device Documentation**

---

### 🔹 Description

The `radio_device` is used to play curated music either directly from the device’s in-world location or for specific players (agents) registered with the device. It can be enabled/disabled, started/stopped by Verse or device wiring, and can manage per-player (agent) music experiences.

---

### 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- radio\_device

---

### 🛠️ Functions & Methods

| Name                        | Description                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------- |
| `Enable()`                  | Enables the device for music playback.                                                 |
| `Disable()`                 | Disables the device; stops any currently playing audio.                                |
| `Play()`                    | Starts playing audio from the device for all (if in "Hear by All" mode).               |
| `Play(agent)`               | Starts playing audio for the specified agent (if in "Hear by Instigator" mode).        |
| `Stop()`                    | Stops any audio currently playing from the device (for all or for a registered agent). |
| `Register(agent)`           | Adds an agent as a music target; audio plays for that player when `Play()` is called.  |
| `Unregister(agent)`         | Removes a specific agent as a music target.                                            |
| `UnregisterAll()`           | Removes all previously registered agents from the target list.                         |
| `Show()` / `Hide()`         | Shows/hides the device in the world.                                                   |
| `GetTransform()`            | Gets device position, rotation, and scale.                                             |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the radio device.                                                   |

---

### 🎛 Configuration Options (Details Panel)

| Option                      | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| Curated Music Playlist      | Selects which music the radio plays.                               |
| Heard By                    | All Players or Instigator Only.                                    |
| Can Be Triggered by Devices | If enabled, external Verse or device triggers can play/stop music. |
| Music Volume                | Controls volume of playback.                                       |
| Enabled At Game Start       | Turns the radio on or off at the beginning of the game.            |

*All options are set in the Details panel in UEFN when the device is selected.*

---

### 🧩 Events

- The `radio_device` does not emit interactive Verse events but can be fully controlled by Verse code and device links.

---

### 🧰 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

radio_device_example := class(creative_device):

    @editable
    Radio : radio_device = radio_device{}

    @editable
    PlayButton : button_device = button_device{}

    @editable
    StopButton : button_device = button_device{}

    var RegisteredAgents : []agent = array{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to control buttons
        PlayButton.InteractedWithEvent.Subscribe(OnPlayPressed)
        StopButton.InteractedWithEvent.Subscribe(OnStopPressed)

    # Button control handlers
    OnPlayPressed(Agent : agent) : void =
        Radio.Play()
        Print("Radio playing!")

    OnStopPressed(Agent : agent) : void =
        Radio.Stop()
        Print("Radio stopped!")

    # Play radio for all registered agents
    PlayForRegisteredAgents() : void =
        Radio.Play()
        Print("Radio playing for all registered agents!")
```

#### Explanation:

- Reference one `radio_device` and two `button_device`s (for Play and Stop).
- On game begin, it subscribes both buttons to handler functions.
- `OnPlayPressed` calls `Radio.Play()`, starting music according to device’s "Heard By" setting.
- `OnStopPressed` stops playback.
- Use `Register(agent)` to have music play for only selected agents (when "Heard By" is Instigator), and `Unregister(agent)` or `UnregisterAll()` to remove specific or all agents.

---

### How to Use in UEFN

1. **Place the Radio Device & Control Buttons**

   - Drag a `radio_device` into your level.
   - Add two `button_device`s to serve as Play and Stop controls.

2. **Configure Radio Device Options (Details Panel)**

   - Set **Curated Music Playlist** for your desired in-game tracks.
   - Set **Heard By**:
     - "All" for global music.
     - "Instigator" for per-agent (register agents and use Play/Stop with agent input in Verse).

3. **Create & Place Your Verse Device**

   - In Verse Explorer, right-click a folder → *Create New Verse File* (e.g., `radio_device_example.verse`).
   - Click *Create Empty*, paste the sample code, and save.
   - Click *Verse → Build Verse Code* (Ctrl+Shift+B) until successful.

4. **Assign References**

   - In the Details panel for your Verse device, set the `Radio`, `PlayButton`, and `StopButton` references.

5. **Test In-Game**

   - Launch session, use Play/Stop controls, and verify music behavior (all or per-agent).

---

### 🧠 Best Practices

- Use agent registration and per-agent playback for special events, team areas, or private music.
- Unregister agents or all agents as needed for silent gameplay moments.
- Use Verse to create interactive soundscapes that respond to gameplay logic, not just proximity.

---

### ❌ Common Issues & Solutions

| Issue                        | Problem (❌)                             | Solution (✅)                                  |
| ---------------------------- | --------------------------------------- | --------------------------------------------- |
| No music plays               | Device not enabled, or wrong “Heard By” | Enable device, or check agent/register logic  |
| Verse functions “don’t work” | References not set                      | Set all @editable references in Details panel |
| Music doesn’t stop           | Used wrong stop function                | Use Stop() or Stop(agent) per configuration   |

*Note: All device options must be configured both in Details and Verse for correct results. Use “Register/Unregister” and per-agent functions for advanced, player-specific music control.*

