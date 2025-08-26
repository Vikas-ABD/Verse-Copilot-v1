# Vending Machine Device Guide (Unreal Editor for Fortnite - UEFN)

## 🔹 Description
The `vending_machine_device` stores and spawns up to three items, allowing players to cycle between them using a pickaxe hit. You can set item costs, specify resource types (Gold, Wood, Stone, Metal), and configure ammo or team settings. Upon interaction, the item is granted to the player's inventory—optionally requiring payment.

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vending_machine_device`

---

## 🛠️ Main Functions & Methods
| Name               | Description                                                  |
|--------------------|--------------------------------------------------------------|
| `Enable()`         | Enables the vending machine.                                |
| `Disable()`        | Disables the machine (players can’t use it).                |
| `SpawnItem()`      | Spawns the current item to the player or world.             |
| `CycleToNextItem()`| Cycles to the next item in the vending machine.             |

---

## 🧹 Events (Data Members)
| Name               | Type             | Description                                             |
|--------------------|------------------|---------------------------------------------------------|
| `ItemSpawnedEvent` | `listenable(agent)` | Fires when an item is spawned, passing the agent who used it. |

---

## 🎠 Key Device Options (Details Panel)
- **First/Second/Third Item**: Drop items in Create mode to register.
- **Resource Type/Cost**: Set Gold/Wood/Stone/Metal and the amount.
- **Initial/Spare Ammo**: Configure ammo amount with weapons.
- **Enabled at Game Start**: Toggle whether the machine is active at game start.
- **Interaction Time**: Choose instant or hold-to-interact.
- **Model**: Change machine's appearance.
- **Selected Team/Class**: Restrict usage by team/class.

---

## 💡 How to Add Items
1. Enter Create mode.
2. Stand in front of the vending machine.
3. Open your inventory and drop up to three different items in front of it.
4. Items will register and display.

---

## 🪠 Verse Example: Control & Events
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

vending_machine_example := class(creative_device):

    @editable
    VendingMachine : vending_machine_device = vending_machine_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    SpawnButton : button_device = button_device{}

    var IsEnabled : logic = true

    OnBegin<override>()<suspends> : void =
        VendingMachine.ItemSpawnedEvent.Subscribe(OnItemSpawned)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawn)

    OnItemSpawned(Agent : agent) : void =
        Print("Item spawned from vending machine!")

    OnEnable(Agent : agent) : void =
        if (IsEnabled = false):
            VendingMachine.Enable()
            set IsEnabled = true
            Print("Vending machine enabled")

    OnDisable(Agent : agent) : void =
        if (IsEnabled = true):
            VendingMachine.Disable()
            set IsEnabled = false
            Print("Vending machine disabled")

    OnSpawn(Agent : agent) : void =
        if (IsEnabled = true):
            VendingMachine.SpawnItem()
            Print("Item spawned from vending machine")
```

### Explanation:
- Adds editable references to a vending machine and three control buttons.
- Subscribes to spawn and interaction events.
- Enables, disables, or spawns an item via buttons.
- Prints logs for debugging/testing.

---

## 💪 UEFN Step-by-Step Setup
### 1. Create the Verse File & Device
- Go to **Verse → Verse Explorer**
- Right-click folder → Create New Verse File (e.g., `vending_machine_example`)
- Paste the Verse code and **Build** (Ctrl+Shift+B)

### 2. Place Devices in Level
- Drag `vending_machine_device` into your level
- Add three `button_device` for Enable, Disable, and Spawn
- Drag your Verse device into the level

### 3. Assign Device References
- Select Verse device → In Details panel:
  - `VendingMachine` → reference to the vending machine
  - `EnableButton`, `DisableButton`, `SpawnButton` → assign button devices

### 4. Add Items to Machine
- In Create mode:
  - Equip and drop desired items in front of the machine (up to 3)

### 5. Configure Options
- In vending machine details:
  - Set **cost**, **ammo**, **team restrictions**, etc.

### 6. Test Gameplay
- Launch session
- Use buttons to control machine
- Monitor logs for debugging

---

## 🧠 Tips
- Hit machine with pickaxe to cycle items.
- One item spawns at a time.
- Use multiple machines for more item options.
- Set different costs for each slot to diversify gameplay.

---

## ❌ Troubleshooting
| Issue                         | Solution                                           |
|-------------------------------|----------------------------------------------------|
| Cannot add more than 3 items | Limit is 3; use multiple vending machines.         |
| Can’t interact in play       | Ensure "Enabled at Game Start" is checked or call `Enable()`. |
| Item not granted             | Check item cost/resource type and slot availability. |

---

## 📅 Note
All vending logic (cost, interaction, cycling) is handled by the device itself. Verse is used for control, automation, and event-driven gameplay logic.

