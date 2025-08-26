# class_selector_ui_device – UEFN Verse Device Documentation

## 🔹 Description
The `class_selector_ui_device` provides a UI interface that lets players choose their class during gameplay. This is commonly used in class-based games, loadout selection, or role-based experiences. It includes events for when the UI is opened or closed and when a class is selected or changed.

## 📁 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `class_selector_ui_device`

## 🦩 Events (Data Members)
| Event Name          | Type                      | Description                                                |
|---------------------|---------------------------|------------------------------------------------------------|
| ClassSelectedEvent  | `listenable(agent)`       | Fires when an agent selects a class (first time).          |
| ClassChangedEvent   | `listenable(tuple<agent, int>)` | Fires when an agent changes their class. Returns agent and selected class index. |
| UIOpenedEvent       | `listenable(agent)`       | Fires when the UI is shown to a player.                    |
| UIClosedEvent       | `listenable(agent)`       | Fires when a player closes the UI.                         |

## 🛠️ Functions & Methods
| Function Name         | Description                                                 |
|-----------------------|-------------------------------------------------------------|
| `Show(Agent: agent)`  | Opens the class selector UI for the specified agent.        |
| `Enable()`            | Enables the device so it can be used.                       |
| `Disable()`           | Disables the device, preventing interaction.                |
| `GetTransform()`      | Returns the transform (position, rotation, scale). Use `IsValid()` check first. |
| `MoveTo(Position, Rotation, Duration)` | Smoothly moves the device over time.                    |
| `MoveTo(Transform, Duration)` | Moves the device using a full transform.              |
| `TeleportTo(...)`     | Instantly moves the device to a new position and rotation.  |

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

class_selector_example := class(creative_device):

    @editable
    ClassSelector : class_selector_ui_device = class_selector_ui_device{}

    OnBegin<override>()<suspends> : void =
        ClassSelector.Enable()
        ClassSelector.ClassSelectedEvent.Subscribe(OnClassSelected)
        ClassSelector.ClassChangedEvent.Subscribe(OnClassChanged)

        # Show to first player who joins
        loop:
            AllPlayers := GetPlayspace().GetPlayers()
            if (AllPlayers.Length > 0):
                ClassSelector.Show(AllPlayers[0])
                break
            Sleep(0.5)

    OnClassSelected(Player : agent) : void =
        Print("Class selected by: {Player}")

    OnClassChanged(Data : tuple<agent, int>) : void =
        let (Player, ClassIndex) = Data
        Print("Player {Player} changed to class index: {ClassIndex}")
```

## 🔧 How to Use in UEFN
1. **Place the Device**
   - Add the `class_selector_ui_device` to your level.

2. **Configure Class Options**
   - In the Details panel, set available classes (defined in `class_selector_device` or class management tools).

3. **Create Verse Script**
   - Use or customize the example script to show the UI and respond to selection.

4. **Assign References**
   - Assign your `ClassSelector` reference in the Verse class's Details panel.

5. **Build & Test**
   - Compile the Verse script (`Ctrl+Shift+B`), enter playtest mode, and verify the UI appears and selections work.

## 🨀 Best Practices
- Use `ClassChangedEvent` to apply class-specific logic, such as equipment, abilities, or team rules.
- Pair with the `class_selector_device` to define what each class gives (items, health, abilities, etc.).
- Call `Show(agent)` from triggers, buttons, or spawn logic to let players change classes mid-game.

## ❌ Common Issues & Solutions
| Issue                  | Problem ❌                          | Solution ✅                                              |
|------------------------|----------------------------------------|-------------------------------------------------------------|
| UI doesn’t appear       | Device not enabled or `Show()` not called | Use `Enable()` and call `Show(agent)`                        |
| Class doesn’t apply     | Class not configured in selector        | Define classes using `class_selector_device`                |
| Event doesn’t fire      | Event not subscribed                    | Use `.Subscribe()` in `OnBegin()`                           |
| UI shows to wrong player | Wrong agent used in `Show()`            | Confirm correct agent reference is passed                   |

## 📌 Note
This device only displays the UI. The actual class definitions and assignments must be managed using `class_selector_device` or class configuration in the Details panel.

