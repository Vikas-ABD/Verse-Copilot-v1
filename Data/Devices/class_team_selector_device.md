# UEFN Verse Device Documentation: `class_and_team_selector_device`

## 📙 Description
The `class_and_team_selector_device` works in conjunction with the `class_designer_device` to control how and when players (agents) can select, change, or be assigned to specific custom classes and teams during gameplay. It supports both manual and automated switching and can be triggered via buttons or other devices.

---

## 🛠️ Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `class_and_team_selector_device`

---

## 🧹 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| `ClassSwitchedEvent` | `listenable(agent)` | Fires when an agent changes class. |
| `TeamSwitchedEvent` | `listenable(agent)` | Fires when an agent changes teams. |

---

## 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables the device for class/team selection. |
| `Disable()` | Disables interaction and switching. |
| `ChangeClass(agent)` | Changes the specified agent's class. |
| `ChangeTeam(agent)` | Changes the specified agent's team. |
| `ChangeTeamAndClass(agent)` | Changes both the team and class of the agent. |
| `ChangeSelectorTeam(agent)` | Assigns agent to control/select for their team (advanced). |

---

## 🔎 Configuration Options (Details Panel)
- **Class to Switch To**: Choose using Class Identifier (linked to `class_designer_device`).
- **Activate Team**: Teams allowed to interact with this device.
- **Team To Switch To**: Which team the agent switches to (can be "Random").
- **Respawn Player On Switch**: Toggle respawn behavior.
- **Restore Health and Shields on Switch**: Heal after switch.
- **Clear Items on Switch**: Options to remove inventory (Team/Class/Always/Never).
- **Time to Switch**: Delay (seconds) before applying switch.
- **Volume Size/Visibility**: Adjust in-world activation volume and visibility.

---

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

class_and_team_selector_example := class(creative_device):

    @editable
    ClassSelector : class_and_team_selector_device = class_and_team_selector_device{}

    @editable
    ClassDesigner : class_designer_device = class_designer_device{}

    @editable
    SelectButton : button_device = button_device{}

    @editable
    ChangeTeamButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SelectButton.InteractedWithEvent.Subscribe(OnSelectPressed)
        ChangeTeamButton.InteractedWithEvent.Subscribe(OnChangeTeamPressed)

    OnSelectPressed(Agent : agent) : void =
        ClassSelector.ChangeClass(Agent)
        Print("Class changed for agent!")

    OnChangeTeamPressed(Agent : agent) : void =
        if (CurrentTeam := GetPlayspace().GetTeamCollection().GetTeam[Agent]):
            Teams := GetPlayspace().GetTeamCollection().GetTeams()
            if (Teams.Length > 1):
                var NextTeamIndex : int = 0
                for (Index -> Team : Teams, Team = CurrentTeam):
                    set NextTeamIndex = Index + 1
                if (NextTeamIndex >= Teams.Length):
                    set NextTeamIndex = 0
                if (NextTeam := Teams[NextTeamIndex]):
                    ClassSelector.ChangeTeam(Agent)
                    Print("Team changed for agent!")
```

---

## 📚 How It Works in UEFN
1. **Create Classes in Class Designer**
   - Add `class_designer_device`s and configure each with class settings and identifiers.

2. **Place Class and Team Selector Device**
   - Drag the `class_and_team_selector_device` onto your map.

3. **Optional: Add Buttons or Interactive Devices**
   - Use `button_device`s to let players trigger switches.

4. **Configure Device in Details Panel**
   - Set "Class to Switch To", "Team To Switch To", and other options.

5. **Create & Build Verse Script**
   - Create new Verse file in Verse Explorer.
   - Paste the script, save, then build with CTRL+SHIFT+B.

6. **Place and Reference Verse Device**
   - Drag the compiled Verse device into your island.
   - Set all `@editable` references in the Details panel.

7. **Test Gameplay**
   - Run a session and interact with buttons. Observe class/team switching and check printed logs.

---

## 🧠 Best Practices
- Assign unique identifiers in each `class_designer_device`.
- Use `.ClassSwitchedEvent.Subscribe(...)` and `.TeamSwitchedEvent.Subscribe(...)` to trigger custom logic.
- Pair with UI or triggers for a custom class picker experience.

---

## ❌ Common Issues & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|--------------------|----------------------|-------------|
| Not assigning class ID | Left "Class To Switch To" blank | Use correct class ID | Device must know the target class |
| Missing team switch | Only class changes | Set "Team To Switch To" | Both team and class should be specified |
| Ignored switch events | No Verse logic on switch | Use `.Subscribe(...)` methods | Required for custom effects |
| Missing device refs | `@editable` fields blank | Assign all refs | Needed to work with Verse |

---

## 🔹 Notes
- Chain multiple selector devices for advanced class/team setups.
- Default behaviors (respawn, inventory clear, health restore) configured in Details panel.
- Essential device for controlled, interactive class/team mechanics in your game.

---

**End of Document**

