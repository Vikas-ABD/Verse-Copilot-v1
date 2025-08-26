📘 conversation_device – UEFN Verse Device Documentation

🔹 Description
The conversation_device in Unreal Editor for Fortnite (UEFN) allows creators to trigger and manage conversations with players using the Conversation Graph. It handles speech nodes, UI display settings, multiple participants, and allows fine-grained control over the flow and termination of conversations via Verse. This device can show names, display text in worldspace, control the speed of speech rendering, and listen/respond to player input.

🧱 Verse Using Statement
verse
CopyEdit
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* conversation_device

🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| Enable() | Enables the device to listen for input and start conversations. |
| Disable() | Disables the device from initiating or managing conversations. |
| InitiateConversation(agent) | Starts the assigned conversation with the specified agent. |
| EndConversation(agent) | Ends the active conversation for a specific agent. |
| EndConversationForAll() | Ends all conversations currently active on this device. |
| GetActiveConversationsCount() | Returns the current number of active conversations. |
| CanInitiateConversation(agent) | Checks if a conversation can be started with the specified agent. |
| IsAgentInConversation(agent) | Checks if an agent is currently in conversation. |
| IsEnabled() | Returns whether the device is enabled. |
| ShowConversation(agent) | Displays the conversation UI for a specific agent. |
| HideConversation(agent) | Hides the conversation UI for the agent. Disables choices. |
| GetTransform() | Gets the device's world transform (location, rotation, scale). |
| MoveTo(Vector3, Rot, Time) | Moves the device to the given position/rotation over time. |
| TeleportTo(Vector3, Rot) | Instantly teleports the device to the given position and rotation. |

🎛 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| AllowedConversationCount | Sets the max number of simultaneous conversations. |
| CharactersPerSecond | Controls how fast characters in speech nodes are revealed (0.25–100.0). |
| ShowConversationTextInWorldSpace | Toggle whether text appears in worldspace for Radial UI. |
| ShowIndicatorBubble | Toggles whether an indicator bubble appears near the device. |
| IndicatorBubbleRange | Range (0–25) at which the indicator bubble appears. |
| ShowNameWhenNearby | Shows the speaker's name when the player is nearby. |
| SpeakerName | Custom name shown as the speaker in conversations. |

📡 Event Signals
| Event | Description |
|-------|-------------|
| OnConversationEvent(payload) | Triggered when a conversation choice is selected. |
| EndEvent(payload) | Fired when a conversation completes. |
| CancelEvent(payload) | Fired if a conversation ends early (e.g., via EndConversation). |

🧠 Verse Usage Example
Here’s a practical example showing how to enable, start, end, and show/hide a conversation for an agent using button devices:

verse
CopyEdit
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

conversation_demo := class(creative_device):

    @editable
    ConversationDevice : conversation_device = conversation_device{}

    @editable
    StartButton : button_device = button_device{}

    @editable
    EndButton : button_device = button_device{}

    @editable
    ShowButton : button_device = button_device{}

    @editable
    HideButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        StartButton.InteractedWithEvent.Subscribe(OnStart)
        EndButton.InteractedWithEvent.Subscribe(OnEnd)
        ShowButton.InteractedWithEvent.Subscribe(OnShow)
        HideButton.InteractedWithEvent.Subscribe(OnHide)

    OnStart(agent : agent) : void =
        if (ConversationDevice.CanInitiateConversation(agent)):
            ConversationDevice.InitiateConversation(agent)
            Print("Conversation started")
        else:
            Print("Cannot start conversation")

    OnEnd(agent : agent) : void =
        ConversationDevice.EndConversation(agent)
        Print("Conversation ended")

    OnShow(agent : agent) : void =
        ConversationDevice.ShowConversation(agent)
        Print("Conversation UI shown")

    OnHide(agent : agent) : void =
        ConversationDevice.HideConversation(agent)
        Print("Conversation UI hidden")

🧹 How This Works
* Enable/Disable: Turns conversation capabilities on or off.
* Initiate/End: Manages when a player can start or exit a conversation.
* Show/Hide UI: Controls visibility of the conversation UI.
* Custom Settings: Customize name, UI location, and reveal speed in the Details panel.
* Events: Hook into events like choice selections or early exits for advanced logic.

🚀 How to Use in UEFN
1. Place the Devices
    * Add a conversation_device to your level.
    * Place buttons to control start, end, show, and hide.
2. Configure Settings
    * Customize name, UI behavior, and character speed in the Details panel.
3. Create a Verse Script
    * Open Verse Explorer, create a new .verse file (e.g., conversation_demo.verse), paste the code, and build it.
4. Assign Editable Fields
    * Link the conversation_device and button_device properties via the Details panel.
5. Test in Session
    * Start your island session, interact with buttons, and verify conversation behavior.

