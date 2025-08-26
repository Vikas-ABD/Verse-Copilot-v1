📘 class_designer_device – UEFN Verse Device Documentation

🔹 Description
The class_designer_device allows creators to design custom classes in Fortnite experiences. Each instance defines a unique class with configurable attributes like health, shield, abilities, and an inventory loadout. These devices work in tandem with class selector devices to create gameplay based on class selection, including Gun Game and role-based classes.

📁 Inheritance Hierarchy
* creative_object
* creative_device_base
* class_designer_device

🛠️ Functions & Methods
| Name               | Description |
|--------------------|-------------|
| GetClassMembers()  | Returns an array of agents currently assigned to this class. |
| IsOfClass(agent)   | Returns true if the given agent is assigned to this class. |
| GetTransform()     | Gets device’s position, rotation, and scale. |
| MoveTo()/TeleportTo() | Moves or teleports the device. Useful for dynamic environments or visual scripting. |

🎮 Configuration Options (Details Panel)
* **Class Identifier** – Unique number required by selector devices.
* **Class Name** – Display/UI name (max 24 chars).
* **Class Description** – Up to 512 characters.
* **Grant Items On Respawn** – Re-give items on agent respawn.
* **Equip Granted Item** – Choose which item is equipped on respawn.
* **Initial/Spare Weapon Ammo** – Ammo override settings.
* **Health/Shield Settings** – Max health, recharge control, shield percentages.
* **Player Abilities** – Enable/disable sprint, slide, mantle, etc.
* **Invincibility** – Toggle for invulnerable classes.
* **Start With Pickaxe** – Determines if a pickaxe is part of loadout.
* **Visible During Game** – Toggle visibility.

🧰 Inventory Setup
* Drop items from content browser onto each class_designer_device to define starting inventory.
* Order matters for “Equip Granted Item”.
* Devices can be renamed for clarity.

🤖 Selector Device Integration
* Use **class_and_team_selector_device** or **class_selector_device** for player class assignment.
* Reference each class by its **Class Identifier**.
* Overrides Island/Team settings when active.

📒 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

class_designer_example := class(creative_device):

    @editable
    ClassDesigner : class_designer_device = class_designer_device{}

    @editable
    ClassSelector : class_and_team_selector_device = class_and_team_selector_device{}

    @editable
    SelectButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        ClassSelector.ClassSwitchedEvent.Subscribe(OnClassSwitched)
        ClassSelector.TeamSwitchedEvent.Subscribe(OnTeamSwitched)
        SelectButton.InteractedWithEvent.Subscribe(OnSelectPressed)

    OnClassSwitched(Agent : agent) : void =
        Print("Class switched for agent!")

    OnTeamSwitched(Agent : agent) : void =
        Print("Team switched for agent!")

    OnSelectPressed(Agent : agent) : void =
        ClassSelector.ChangeClass(Agent)
        Print("Class changed for agent!")
```

📚 How It Works in UEFN
1. **Place Class Designer Devices**
   * Each class gets its own class_designer_device.
   * Drop items on each device in editor to define inventory.

2. **Configure Attributes in Details Panel**
   * Set identifier, name, description, health/shield values, and abilities.

3. **Add Selector Devices**
   * Use class_and_team_selector_device or class_selector_device.
   * Reference Class Identifier values.

4. **Write & Build Verse Script**
   * Create a Verse file and paste example.
   * Build via Verse → Build Verse Code (Ctrl+Shift+B).

5. **Place & Reference Verse Device**
   * Add the Verse device and configure the @editable references.

6. **Test the Experience**
   * Interact with button and verify log output.
   * Check for correct class switch and inventory.

🧠 Best Practices
* Use unique Class Identifiers and document them.
* Combine selectors and scripting for progressive roles.
* Track agents using GetClassMembers() for team logic.
* Use IsOfClass(agent) for conditional logic.
* Order loadout carefully if using Equip Granted Item.

❌ Common Issues & Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|------------|--------------|-------------|
| Missing Identifier | Default value | Unique number | Required for class selection |
| One device per class | One device with many configs | One device per class | Each device defines one class |
| Selector misconfigured | Wrong ID | Use correct Class Identifier | IDs must match |
| Referencing class by name in code | String name | Use device reference | Always use @editable reference |
| Forgetting inventory setup | No items on device | Drop each item onto class_designer_device | Defines loadout |

🔹 Notes
* Class updates only affect new class switches/respawns.
* Use this device with a selector for role-based, Gun Game, or class kit gameplay systems.

