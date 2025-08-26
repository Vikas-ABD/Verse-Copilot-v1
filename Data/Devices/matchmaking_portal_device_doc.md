## 📘 Matchmaking Portal Device – UEFN Verse Device Documentation

### 🔹 Description
The `matchmaking_portal_device` is used to send players to other islands and link experiences together. It can create portals in your Fortnite island that transfer players to another island via the specified island code. This device enables cross-island hub designs, multi-stage game flows, and creative map navigation. Portal activation can be managed via direct event binding, Verse, or button/trigger logic.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `matchmaking_portal_device`

---

### 🛠️ Functions & Methods
| Name     | Description                          |
|----------|--------------------------------------|
| Enable() | Makes the portal usable and visible. |
| Disable()| Disables/fades out the portal.       |

---

### 🎛 Configuration Options (Details Panel)
| Option                     | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| Island Code               | The destination island code the portal links to.                  |
| Set Island Title Visibility | Show/hide island name on player hover.                            |
| Set Island Details Visibility | Show/hide description/details.                                   |
| Visible During Game       | Portal visible during gameplay or only in pregame.                |
| Enable Audio              | Ambient sound effect on/off.                                       |
| Enable as Art             | If Yes, portal is a static prop, not usable as a portal.           |
| Code Override Allowed     | Whether players can override the destination code from UI.         |
| Join Option               | Public Only, Private Only, Player Chooses.                         |
| Light Strength            | Sets light/intensity effect of the portal.                         |
| Code Override Cooldown    | Cooldown time before override is allowed again.                    |
| After Cooldown            | Reset to original or keep overridden code after cooldown.          |

> Note: All main options are set in the Details panel for the portal.

---

### 🧩 Events
This device does not expose Verse-invocable events but can be directly controlled via Verse or creative device binding.

---

### 🧰 Verse Usage Example
Basic control of a matchmaking portal using Verse and buttons for enable/disable actions:
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

matchmaking_portal_example := class(creative_device):

    @editable
    MatchmakingPortal : matchmaking_portal_device = matchmaking_portal_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        MatchmakingPortal.Enable()
        Print("Matchmaking portal enabled!")

    OnDisablePressed(Agent : agent) : void =
        MatchmakingPortal.Disable()
        Print("Matchmaking portal disabled!")
```

#### Explanation:
- Reference the `matchmaking_portal_device` and two `button_devices`.
- Pressing a button enables or disables the portal.
- All visual/audio/configuration is done in the Details panel.

---

### 🚀 How to Use in UEFN

**1. Place the Portal**
- In the Content Browser, drag in a `matchmaking_portal_device` to the world.

**2. Configure Portal Options**
- In the Details panel, set:
  - Island Code (destination experience)
  - Visibility, audio, override, and access options as needed.

**3. (Optional) Place Control Devices**
- Add two `button_devices` (one to enable, one to disable).

**4. Create and Place Verse Device**
- In Verse Explorer:
  - Right-click a folder → Create New Verse File (e.g., `matchmaking_portal_example.verse`)
  - Paste the sample code, save.
  - Build Verse Code (Ctrl+Shift+B) until “Build Succeeded” appears.
  - Place your Verse device into the level.
  - In its Details panel, set:
    - MatchmakingPortal → your portal
    - EnableButton / DisableButton → your button devices

**5. Test the Experience**
- In play mode, pressing the buttons enables or disables the portal.

---

### 🧠 Best Practices
- For multi-island or hub navigation, use one portal per destination.
- Use `.Enable()`/`.Disable()` for story progress, puzzles, or unlocks.
- Configure all options (code, visuals, access) in the Details panel before gameplay.

---

### ❌ Common Issues & Fixes
| Issue                       | ❌ Example Problem                  | ✅ Correct Solution                         | Explanation                                  |
|----------------------------|------------------------------------|--------------------------------------------|----------------------------------------------|
| Portal does not work       | No island code or disabled         | Set valid island code, enable device        | Portal must be enabled to function           |
| Can't control via buttons  | Did not assign @editable fields    | Assign in Details panel after placement     | Refs must be manually set in Details panel   |
| Event binding unclear      | Tried to listen to events          | Use `.Enable()`/`.Disable()` instead        | Events not directly exposed                  |
| Portals open when not wanted | Portal left enabled permanently  | Control with Verse script/buttons           | Prevents unintended player movement          |

---

### 📌 Notes
- Ideal for advanced multi-stage experiences and hubs.
- All visual/audio/navigation settings handled in Details.
- Real-time control (enable/disable) handled via Verse or events.

