📘 sword\_in\_the\_stone\_device – UEFN Verse Device Documentation

🔹 Description The sword\_in\_the\_stone\_device is a special creative device used to spawn and place the Infinity Blade on your island. Once placed, any player regardless of team can claim and wield the blade. It does not contain event listeners or traditional interaction logic, but supports transform-based manipulation via Verse.

🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- sword\_in\_the\_stone\_device

🛠️ Functions & Methods

| Name                                                           | Description                                                                                                                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GetTransform()                                                 | Returns the current transform (position, rotation, scale) of the device. Values are in centimeters. You must check if the object is valid via IsValid() to avoid runtime errors. |
| MoveTo(Position: vector3, Rotation: rotation, Duration: float) | Smoothly moves the device to a new position and rotation over time (in seconds). Interrupts any ongoing animations.                                                              |
| MoveTo(Transform: transform, Duration: float)                  | Moves the device using a full transform struct (position, rotation, scale) over time.                                                                                            |
| TeleportTo(Position: vector3, Rotation: rotation)              | Instantly teleports the device to a new position and rotation.                                                                                                                   |
| TeleportTo(Transform: transform)                               | Instantly teleports to a full transform (position, rotation, scale).                                                                                                             |

🎛️ Configuration Options (Details Panel) This device does not expose custom configuration options like scoring or events. Instead, the presence of the Infinity Blade itself determines interaction. You can control the device’s placement, movement, and behavior through Verse or sequence triggers.

🧰 Verse Usage Example Here's a minimal Verse example demonstrating how to move the sword dynamically during gameplay:

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

sword_move_example := class(creative_device):

    @editable
    Sword : sword_in_the_stone_device = sword_in_the_stone_device{}

    OnBegin<override>()<suspends> : void =
        if (Sword.IsValid()):
            Print("Sword is valid. Moving to a new location.")
            Sword.MoveTo(
                Position := vector3{X := 0.0, Y := 1000.0, Z := 200.0},
                Rotation := rotation{Pitch := 0.0, Yaw := 180.0, Roll := 0.0},
                Duration := 3.0
            )
```

🔧 How to Use in UEFN

1. **Place the Device**
   - In the Devices tab, add the Sword in the Stone device to your island.
2. **Configure Transform**
   - Adjust its initial position, rotation, and visibility in the Details panel.
3. **Create a Verse File**
   - In Verse Explorer: Right-click → Create New Verse File, e.g., `sword_move_example.verse`.
   - Paste the example code above.
   - Build Verse code using Ctrl+Shift+B until "Build Succeeded".
4. **Assign References**
   - In the Details panel of your custom Verse device, assign the `Sword` field to your `sword_in_the_stone_device`.
5. **Test**
   - Start the experience. If Verse is triggered on begin, the sword will move as scripted.

🧠 Best Practices

- Use `IsValid()` before calling any functions to prevent runtime errors.
- Combine with triggers or timers to animate sword movement during gameplay.
- Although no native events are exposed, use buttons, triggers, or collision volumes to control the sword dynamically.

❌ Common Issues & Solutions

| Issue                     | Problem (❌)                              | Solution (✅)                                       |
| ------------------------- | ---------------------------------------- | -------------------------------------------------- |
| Script crashes or fails   | Did not check `IsValid()` before calling | Always use `if (Sword.IsValid())` before movement  |
| Infinity Blade not usable | Player can't interact                    | Make sure device is enabled and accessible in-game |
| No events available       | Expecting event listeners like hits      | Use external triggers or buttons for logic flow    |

📌 Note: The `sword_in_the_stone_device` is a static interaction device — it allows players to pick up the Infinity Blade, but doesn't provide its own Verse events like `InteractedWithEvent`. Control logic must be done through external triggers or placement/movement via Verse.

