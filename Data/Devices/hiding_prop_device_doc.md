📘 **hiding_prop_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `hiding_prop_device` allows players to hide inside special props (e.g., haystacks, dumpsters, or port-a-potties) on your Fortnite island. It supports “Hidden Travel,” enabling teleportation between configured hiding props. You can control occupancy limits, ejection rules, travel groups, and trigger logic for player entry/exit.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `hiding_prop_device`

---

### 🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| `BeginPlayerHideEvent` | `listenable(agent)` | Fires when a player hides in this prop. |
| `EndPlayerHideEvent` | `listenable(agent)` | Fires when a player exits hiding in this prop. |
| `PlayerHiddenTravelEvent` | `listenable(agent)` | Fires after a player completes hidden travel. |

---

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables the prop. Players can hide/interact. |
| `Disable()` | Disables the prop. Players can’t interact/hide. |
| `EjectAllHiddenPlayers()` | Ejects all players hiding in this prop. Returns array of ejected players. |
| `EjectHiddenPlayer(agent)` | Ejects a specific player from the prop. |
| `HideNearbyPlayers(Radius:float)` | Hides players within specified radius (meters), respecting max occupants. |
| `MoveTo(...) / TeleportTo(...)` | Move or teleport prop. |
| `IsEnabled()` | Returns true if prop is enabled. |

---

### 🎛 Configuration Options (Details Panel)
- **Enabled at Game Start** – Toggle to allow hiding from the start.
- **Usable by Team/Class** – Restrict who can hide.
- **Max Number of Occupants** – Limit simultaneous hiders.
- **Should Wobble While Hiding** – Adds visual/aural effects.
- **Max Hiding Time** – Eject after timeout.
- **Block Hide Time** – Cooldown after a player exits.
- **Hidden Travel Group/Target Group** – Enable teleportation between props.
- **Attempt No Repeat Destinations** – Avoid previous hiding prop.
- **Eject When Failing Requirements** – Eject if requirements change mid-hide.

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

hiding_prop_example := class(creative_device):

    @editable
    HidingProp : prop_mover_device = prop_mover_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    EjectButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        EjectButton.InteractedWithEvent.Subscribe(OnEjectPressed)

    OnEnablePressed(Agent : agent) : void =
        HidingProp.Enable()
        Print("Hiding prop enabled!")

    OnDisablePressed(Agent : agent) : void =
        HidingProp.Disable()
        Print("Hiding prop disabled!")

    OnEjectPressed(Agent : agent) : void =
        Print("Eject function called - implement custom logic if needed!")
```

---

### 🔧 How it Works in UEFN
1. **Place Devices in Level**
   - Use props from the Hiding Prop Gallery.
   - For hidden travel, set the *Hidden Travel Group*.

2. **Configure in Details Panel**
   - Set occupants, wobble effects, timeouts, ejection behavior, team/class restrictions.

3. **Create & Build Verse Script**
   - Add Verse file (e.g., `hiding_prop_example.verse`) and paste code.
   - Build: `Verse → Build Verse Code` (or CTRL+SHIFT+B).

4. **Place & Assign Verse Device**
   - Drag `hiding_prop_example` into your level.
   - Assign device references (HidingProp, EnableButton, etc.).

5. **Test**
   - Launch session and test interactions, teleportation, and Verse-controlled logic.

---

### 🧠 Best Practices
- Use only props from the Hiding Prop Gallery.
- Set consistent travel groups for teleportation.
- Use team/class restrictions for asymmetric gameplay.
- Call `.EjectAllHiddenPlayers()` at end of round or reset.
- Use entry/exit events for dynamic feedback (score, sounds, etc.).

---

### ❌ Common Mistakes & Fixes
| Issue | ❌ Wrong Usage | ✅ Correct Usage | Explanation |
|-------|----------------|------------------|-------------|
| Standard props used | Non-compatible props | Use Hiding Prop Gallery | Other props lack hiding behavior |
| Missing travel group | No teleportation | Set same group on all travel props | Enables hidden travel |
| Trying mid-game toggle via UI | Won’t apply changes | Use `Enable()`/`Disable()` in Verse | Dynamic changes need scripting |
| No event subscriptions | No feedback or logic triggers | Subscribe to `BeginPlayerHideEvent` etc. | All logic must be event-driven |

---

### 📝 Notes
- Use `EjectAllHiddenPlayers` and `HideNearbyPlayers` for bulk behavior.
- Ideal for stealth, puzzle, or prop-hunt gameplay.
- All behavior can be controlled or extended via Verse scripting.

