import os
import getpass
import logging
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# --- Configure Logging and Environment ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()
logger.info("Environment variables loaded if .env file exists.")


# --- Configuration ---
# Set the path where you want to store the Chroma database locally.
PERSIST_DIRECTORY = "./Device_context_db"

def ingest_manual_device_data_faiss():
    """
    Creates a Chroma vector database from a manually defined list of LangChain
    Documents and persists it to disk.
    """
    # --- 1. Set up Google API Key and Embeddings Model ---
    # Will prompt for the key if the environment variable is not set.
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API Key: ")

    print("Initializing Google Generative AI Embeddings with 'models/text-embedding-004'...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    # --- 2. Manually Define Your Documents Here ---
    print("\nUsing manually defined list of documents...")
    
    manual_documents = [
        Document(
            page_content="Device Name: player_spawn_device",
            metadata={"info": """player_spawn_device – UEFN Verse Device Documentation
### 🔹 Description
The player_spawn_device controls where and how players spawn or respawn in your island. You can dynamically enable/disable spawn points, teleport players to specific spawns, and respond to spawn events through Verse code.

This device is essential for creating custom respawn logic, team-based spawning, checkpoint systems, or event-triggered player positioning.

### 🧱 Imports Required
Include these at the top of your Verse file:

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Playspace }
```

### 🔁 Main Event
**PlayerSpawnedEvent**
Description: Fires when a player spawns at this spawn device.

Event Signal:
```verse
PlayerSpawnedEvent: listenable(agent)
```

Correct Handler Signature:
```verse
OnPlayerSpawned(Player: agent): void = ...
```

Subscription Example:
```verse
MySpawn.PlayerSpawnedEvent.Subscribe(OnPlayerSpawned)
```

### 🧰 Core Methods
| Method | Signature | Description |
|--------|-----------|-------------|
| SpawnPlayer | SpawnPlayer(Player: agent): void | Forces a specific player to spawn at this device |
| Enable | Enable(): void | Enables the spawn point for use |
| Disable | Disable(): void | Disables the spawn point |
| IsEnabled | IsEnabled(): logic | Returns whether the spawn is currently enabled |

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Playspace }
using { /UnrealEngine.com/Temporary/Diagnostics }

player_spawn_example_device := class(creative_device):

    @editable
    TeamRedSpawn : player_spawn_device = player_spawn_device{}
    
    @editable
    TeamBlueSpawn : player_spawn_device = player_spawn_device{}

    OnBegin<override>()<suspends>: void =
        TeamRedSpawn.Enable()
        TeamBlueSpawn.Enable()
        
        TeamRedSpawn.PlayerSpawnedEvent.Subscribe(OnRedTeamSpawned)
        TeamBlueSpawn.PlayerSpawnedEvent.Subscribe(OnBlueTeamSpawned)

    OnRedTeamSpawned(Player: agent): void =
        Print("Red team player spawned: {Player}")
        
    OnBlueTeamSpawned(Player: agent): void =
        Print("Blue team player spawned: {Player}")
```)}

### ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong | ✅ Fix |
|-------|----------|--------|
| Wrong handler signature | `OnPlayerSpawned(): void` | Must include agent parameter: `OnPlayerSpawned(Player: agent)` |
| Forgetting to enable | Just calling SpawnPlayer | Call `MySpawn.Enable()` first |
| Invalid player reference | `SpawnPlayer("PlayerName")` | Must pass agent: `SpawnPlayer(PlayerAgent)` |

### 🧠 Best Practices
- Use `@editable` to reference multiple spawn devices for different teams or areas
- Always call `Enable()` before using spawn functionality
- Combine with team assignment devices for proper team-based spawning
- Use `IsEnabled()` to check spawn availability before forcing spawns

Great for:
- Team-based game modes
- Checkpoint systems
- Custom respawn mechanics
- Event-triggered player positioning
"""}
        ),
        Document(
            page_content="Device Name: damage_volume_device",
            metadata={"info": """## 📘 damage_volume_device – UEFN Verse Device Documentation

### 🔹 Description
The damage_volume_device creates an invisible area that damages players when they enter or remain within it. You can control the damage amount, timing, and which players are affected through Verse code.

Perfect for creating hazard zones, environmental damage areas, or timed challenge regions.

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

### 🔁 Main Events
**PlayerDamagedEvent**
Description: Fires when a player takes damage from this volume.

Event Signal:
```verse
PlayerDamagedEvent: listenable(agent)
```

**PlayerEliminatedEvent**
Description: Fires when a player is eliminated by this damage volume.

Event Signal:
```verse
PlayerEliminatedEvent: listenable(agent)
```

### 🧰 Core Methods
| Method | Signature | Description |
|--------|-----------|-------------|
| Enable | Enable(): void | Activates the damage volume |
| Disable | Disable(): void | Deactivates the damage volume |
| SetDamage | SetDamage(Amount: float): void | Changes the damage amount dealt |

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

damage_volume_example_device := class(creative_device):

    @editable
    LavaZone : damage_volume_device = damage_volume_device{}

    OnBegin<override>()<suspends>: void =
        LavaZone.Enable()
        LavaZone.SetDamage(25.0)
        
        LavaZone.PlayerDamagedEvent.Subscribe(OnPlayerDamaged)
        LavaZone.PlayerEliminatedEvent.Subscribe(OnPlayerEliminated)

    OnPlayerDamaged(Player: agent): void =
        Print("Player {Player} took lava damage!")
        
    OnPlayerEliminated(Player: agent): void =
        Print("Player {Player} was eliminated by lava!")
```
"""}
        ),
        Document(
            page_content="Device Name: collectible_device",
            metadata={"info": """## 📘 collectible_device – UEFN Verse Device Documentation

### 🔹 Description
The collectible_device creates items that players can pick up in your island. You can track collection events, respawn collectibles, and control their availability through Verse.

Ideal for creating pickup systems, currency mechanics, or objective-based collection gameplay.

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

### 🔁 Main Event
**CollectedEvent**
Description: Fires when a player collects this item.

Event Signal:
```verse
CollectedEvent: listenable(agent)
```

### 🧰 Core Methods
| Method | Signature | Description |
|--------|-----------|-------------|
| Show | Show(): void | Makes the collectible visible and collectable |
| Hide | Hide(): void | Hides the collectible from players |
| Respawn | Respawn(): void | Respawns the collectible after being collected |
| Enable | Enable(): void | Enables the collectible device |
| Disable | Disable(): void | Disables the device |

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

collectible_example_device := class(creative_device):

    @editable
    GoldCoin : collectible_device = collectible_device{}
    
    var PlayerScore : int = 0

    OnBegin<override>()<suspends>: void =
        GoldCoin.Enable()
        GoldCoin.Show()
        GoldCoin.CollectedEvent.Subscribe(OnCoinCollected)

    OnCoinCollected(Player: agent): void =
        set PlayerScore = PlayerScore + 10
        Print("Player {Player} collected coin! Score: {PlayerScore}")
        
        # Respawn after 5 seconds
        spawn { RespawnAfterDelay(5.0) }

    RespawnAfterDelay(Delay: float)<suspends>: void =
        Sleep(Delay)
        GoldCoin.Respawn()
        GoldCoin.Show()
```
"""}
        ),
        Document(
            page_content="Device Name: capture_area_device",
            metadata={"info": """## 📘 capture_area_device – UEFN Verse Device Documentation

### 🔹 Description
The capture_area_device creates zones that players or teams can capture and control. You can track capture progress, ownership changes, and implement king-of-the-hill or control point mechanics.

Perfect for competitive game modes involving area control and territorial gameplay.

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

### 🔁 Main Events
**CapturedEvent**
Description: Fires when the area is fully captured by a team.

Event Signal:
```verse
CapturedEvent: listenable(agent)
```

**CapturingEvent**
Description: Fires when capture progress changes.

Event Signal:
```verse
CapturingEvent: listenable(agent)
```

### 🧰 Core Methods
| Method | Signature | Description |
|--------|-----------|-------------|
| StartCapture | StartCapture(): void | Begins the capture process |
| StopCapture | StopCapture(): void | Halts any ongoing capture |
| ResetCapture | ResetCapture(): void | Resets capture progress to zero |
| Enable | Enable(): void | Enables the capture area |
| Disable | Disable(): void | Disables the area |

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

capture_area_example_device := class(creative_device):

    @editable
    ControlPoint : capture_area_device = capture_area_device{}

    OnBegin<override>()<suspends>: void =
        ControlPoint.Enable()
        ControlPoint.CapturedEvent.Subscribe(OnAreaCaptured)
        ControlPoint.CapturingEvent.Subscribe(OnAreaCapturing)

    OnAreaCaptured(Player: agent): void =
        Print("Control point captured by {Player}!")
        
    OnAreaCapturing(Player: agent): void =
        Print("Player {Player} is capturing the control point...")
```
 """}
        ),
        Document(
            page_content="Device Name: team_settings_device",
            metadata={"info": """## 📘 team_settings_device – UEFN Verse Device Documentation

### 🔹 Description
The team_settings_device manages team assignments, team properties, and team-based gameplay mechanics. You can assign players to teams, modify team settings, and respond to team-related events.

Essential for any multi-team game mode or competitive experience.

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Playspace }
```

### 🔁 Main Event
**TeamChangedEvent**
Description: Fires when a player's team assignment changes.

Event Signal:
```verse
TeamChangedEvent: listenable(agent)
```

### 🧰 Core Methods
| Method | Signature | Description |
|--------|-----------|-------------|
| ChangeToTeam | ChangeToTeam(Player: agent, TeamIndex: int): void | Assigns player to specific team |
| GetTeam | GetTeam(Player: agent): int | Returns the player's current team index |
| Enable | Enable(): void | Enables team functionality |
| Disable | Disable(): void | Disables the device |

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Playspace }
using { /UnrealEngine.com/Temporary/Diagnostics }

team_settings_example_device := class(creative_device):

    @editable
    TeamManager : team_settings_device = team_settings_device{}

    OnBegin<override>()<suspends>: void =
        TeamManager.Enable()
        TeamManager.TeamChangedEvent.Subscribe(OnTeamChanged)
        
        # Auto-assign players to teams
        spawn { AssignPlayersToTeams() }

    OnTeamChanged(Player: agent): void =
        TeamIndex := TeamManager.GetTeam(Player)
        Print("Player {Player} assigned to Team {TeamIndex}")

    AssignPlayersToTeams()<suspends>: void =
        AllPlayers := GetAllPlayers()
        for (Index -> Player : AllPlayers):
            TeamIndex := Index mod 2  # Alternate between team 0 and 1
            TeamManager.ChangeToTeam(Player, TeamIndex)
```
"""}
        ),
        # Add more Document objects here as needed
        Document(
            page_content="Device Name: team_settings_and_inventory_device",
            metadata={"info": """
team_settings_and_inventory_device — Full Device Reference
Purpose
The team_settings_and_inventory_device lets you precisely configure team attributes, inventory, and behaviors for team-based game modes. It enables per-team rules, item grants, class overrides, team colors/icons, respawn logic, and exposes Verse events related to team activity.

Key Methods (Verse API)
Method	Description	Example Usage
EndRound()	Ends the round and *the team configured in this device* wins the round.	TeamDevice.EndRound()
IsOnTeam(Agent:agent)<decides>	*Failable*: Succeeds if Agent is on this device’s team.	if (TeamDevice.IsOnTeam[Player]): ...
GetTeamMembers()<reads> : []agent	Returns an array of all current agents (players) on the configured team.	Agents := TeamDevice.GetTeamMembers()
Key Events and Subscriptions
Event Name	Handler Signature	Description	Example Subscription
EnemyEliminatedEvent	(Agent:agent):void	Fires when a member of this team eliminates an enemy. Sends the eliminator.	TeamDevice.EnemyEliminatedEvent.Subscribe(MyFunc)
TeamMemberEliminatedEvent	(Agent:agent):void	Fires when a team member is eliminated. Sends the eliminated agent.	TeamDevice.TeamMemberEliminatedEvent.Subscribe(MyFunc)
TeamMemberSpawnedEvent	(Agent:agent):void	Fires when a team member respawns or spawns. Sends the agent.	TeamDevice.TeamMemberSpawnedEvent.Subscribe(MyFunc)
TeamOutOfRespawnsEvent	():void	Fires when all members of this team run out of respawns.	TeamDevice.TeamOutOfRespawnsEvent.Subscribe(MyFunc)
Correct Handler Signatures (for Subscriptions):
EnemyEliminatedEvent.Subscribe(MyHandler)
MyHandler(Agent:agent):void = ...
TeamMemberEliminatedEvent.Subscribe(MyHandler)
MyHandler(Agent:agent):void = ...
TeamMemberSpawnedEvent.Subscribe(MyHandler)
MyHandler(Agent:agent):void = ...
TeamOutOfRespawnsEvent.Subscribe(MyHandler)
MyHandler():void = ...
Incorrect Examples:
❌ Wrong parameter type: (Result: elimination_result):void
❌ Handler takes no parameters when event sends agent (except for TeamOutOfRespawnsEvent, which sends none)
Typical Verse Setup Example
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
 
# Handler class for team events (optional)
team_event_handler := class:
    OnEnemyEliminated(Agent:agent):void =
        Print("Team member eliminated an enemy: {Agent}")
 
    OnTeamMemberEliminated(Agent:agent):void =
        Print("Team member was eliminated: {Agent}")
 
    OnTeamMemberSpawned(Agent:agent):void =
        Print("Team member spawned: {Agent}")
 
    OnOutOfRespawns():void =
        Print("Team is out of respawns!")
 
team_device_example := class(creative_device):
    @editable
    TeamDevice: team_settings_and_inventory_device = team_settings_and_inventory_device{}
 
    var Handler: team_event_handler = team_event_handler{}
 
    OnBegin<override>()<suspends>:void=
        TeamDevice.EnemyEliminatedEvent.Subscribe(Handler.OnEnemyEliminated)
        TeamDevice.TeamMemberEliminatedEvent.Subscribe(Handler.OnTeamMemberEliminated)
        TeamDevice.TeamMemberSpawnedEvent.Subscribe(Handler.OnTeamMemberSpawned)
        TeamDevice.TeamOutOfRespawnsEvent.Subscribe(Handler.OnOutOfRespawns)

Typical Use Cases
Team Scoreboard: Track and display team-based eliminations or objectives by subscribing to elimination and spawn events.
Team Inventory: Use device’s advanced grant/clear item rules for respawn, defined in Details Panel (not Verse).
Round/Win Control: Use EndRound() method to declare team victory and end the round at any moment.
Custom Team Rules: Query IsOnTeam[Agent] or iterate with GetTeamMembers() for advanced team-based logic.
Device Options (UEFN Details Panel)
Option	Description
Team Name	Name/scoreboard label for HUD.
Team Color	Color for team visuals.
Team	Team index to control which players this config applies to.
Team Icon	HUD icon shown for team.
Default Class Identifier	Overrides for player class if using class system.
Grant Items on Respawn	Give team inventory when respawning.
Grant Condition	Always or Only when inventory is empty.
On-Grant Behavior	Clear all, clear items, or keep all on respawn.
Equip Granted Item	Which item(s) to forcibly equip on respawn.
Initial Weapon Ammo/Spare	Ammo to grant on spawn/respawn.
NOTE: Most config is set via the editor, not Verse!	
Best Practices and Common Mistakes
Aspect	Best Practice	Mistake Example
Subscribing to events	Always match handler signature to event	Passing wrong parameter type or wrong event name
IsOnTeam[Agent] usage	Use as a failable context (if (IsOnTeam[Agent]))	Using as regular function call (will not compile)
Get team members	Use .GetTeamMembers() returns []agent	Attempting to get classes/items via Verse fails
Ending round	Use .EndRound() for correct team win	Calling with agent input or on the wrong instance
Team win/loss logic	Always trigger win via method or event	Relying on score only—doesn't auto end the round
Device-to-player	Get associations via UEFN team assignment/island	Expecting device to "find" team via agent input
Incorrect Usage Examples
❌ TeamDevice.EnemyEliminatedEvent.Subscribe(Foo(Result:elimination_result):void=...)
(Wrong event parameter type)
❌ TeamDevice.CompletedEvent.Subscribe(...)
(No such event)
❌ TeamDevice.IsOnTeam(Player) (Should be TeamDevice.IsOnTeam[Player] and in if or failure context)
❌ TeamDevice.EndRound(Player) (No parameters—must be called with no arguments)
Advanced Example: Checking and Moving All Team Members
verse
for (Member:TeamDevice.GetTeamMembers()):
   if (TeamDevice.IsOnTeam[Member]):
      # Member is on this team, perform logic

Summary Table
What	Correct Example	Incorrect Example
Event Subscription	.EnemyEliminatedEvent.Subscribe(MyHandler)	Wrong event or wrong handler type
Handler Signature	(Agent:agent):void for most events, ():void for out of respawns	(Result: elimination_result):void
Team Controls	.EndRound()	.EndRound(Player) (no params allowed)
Check Team Membership	if (TeamDevice.IsOnTeam[Player]): ...	TeamDevice.IsOnTeam(Player)
Get Members	TeamDevice.GetTeamMembers()	-
Device Does NOT Provide
Direct inventory manipulation via Verse: Item grant/clear is set up with Details Panel, not via Verse.
Inventory-based events: No triggers when items granted directly.
Events for classes or icons: No events/Verse access for config options other than those in table above.
In Summary
Use this device for all per-team rule-sets in Verse.
Subscribe to team events and react in handlers.
Use .EndRound() for round control.
Use .IsOnTeam[] and .GetTeamMembers() for membership logic.
All other config is set up in UEFN’s Details Panel.
Don’t mismatch events or signatures.
"""}
        ),

        Document(
            page_content="Device Name: tracker_device ",
            metadata={"info": """
tracker_device — Full Reference
Purpose
The tracker_device is used to count player, team, or channel-driven progress toward a goal (such as collecting items, performing actions, or receiving signals). When the tracked count meets the target, it triggers its completion logic, and can interact with other devices and Verse code.

Key Methods (Verse API)
Method	Description / Signature	Example Usage
SetTarget(Agent:agent, Value:int)	Sets a custom tracked value for a player. Must be called with a valid player agent.	MyTracker.SetTarget(Player, 5)
SetTitleText(Title:message)	Sets the visible label/title for the tracker to a localized message.	MyTracker.SetTitleText(MyMessage)
IncrementProgress(Agent:agent)	Increases the tracked count for a given agent (player).	MyTracker.IncrementProgress(Player)
ResetProgress(Agent:agent)	Resets progress for the given agent.	MyTracker.ResetProgress(Player)
Enable()	Enables the tracker device.	MyTracker.Enable()
Disable()	Disables the tracker.	MyTracker.Disable()
> Note: Some tracker_device methods are for channel-based tracking set up in the UEFN Details Panel, and not directly callable in Verse.

Key Event(s)
Event Name	Handler Signature	Description	Example Subscription
CompleteEvent	Handler(agent):void	Fires when a given agent completes the tracker objective (reaches goal).	MyTracker.CompleteEvent.Subscribe(OnCompleted)
Example subscription:
verse
MyTracker.CompleteEvent.Subscribe(OnCompleted)
OnCompleted(Agent:agent):void = ... # Agent is the player who completed the tracker

Incorrect:
❌ MyTracker.CompletedEvent.Subscribe(...) — *Incorrect event name*
❌ Handler(Result: elimination_result):void — *Incorrect handler signature*
Typical Setup Example
verse
@editable
MyTracker : tracker_device = tracker_device{}
 
OnBegin<override>()<suspends>:void=
    MyTracker.CompleteEvent.Subscribe(OnTrackerCompleted)
    MyTracker.SetTitleText(StringToMessage("Collect 5 Stars"))
    if (Player := GetPlayspace().GetPlayers()[0]):
        MyTracker.SetTarget(Player, 5)
 
OnTrackerCompleted(Agent:agent):void=
    # Do something when tracker completes for this agent

Common Configuration (Device Details Panel in UEFN)
Stat to Track:
Usually set to "Channel" for signal-based progress, or to in-game actions (eliminations, collections, etc).
Target Value:
The goal (how many events to track before completion).
Reset Between Rounds:
Whether progress resets each round.
Tracker Title:
The label visible to players.
You can also wire up channels for incrementing progress or handling tracker completion if not using Verse.
Correct Event & Subscription Rules
Always use .CompleteEvent (not .CompletedEvent).
Always subscribe with a function that takes a single agent parameter.
Incorrect Usage
Subscribing with the wrong event name (.CompletedEvent, .CompeteEvent, etc.).
Handler function with the wrong parameter type (elimination_result, ?agent, or no parameters).
Passing an array of agents or other types to methods/events.
Calling progress or completion methods outside of a failure context (if required).
Interaction with Other Devices
You can trigger other devices (such as trigger_device, end_game_device, item_granter_device, etc.) upon tracker completion via Verse in the event handler, or by wiring channels in the Details panel.
Verse lets you react programmatically to tracker progress and completion, enabling more dynamic gameplay control.
Quick Example: Awarding an Item When Complete
verse
@editable
MyTracker : tracker_device = tracker_device{}
@editable
RewardTrigger : trigger_device = trigger_device{}
 
OnBegin<override>()<suspends>:void=
    MyTracker.CompleteEvent.Subscribe(OnTrackerCompleted)
 
OnTrackerCompleted(Agent:agent):void=
    RewardTrigger.Trigger(Agent)

Summary Table
What	Correct	Incorrect
Event Name	.CompleteEvent	.CompletedEvent
Handler Sig	(Agent:agent):void	(Result: elimination_result):void or anything else
SetTarget	SetTarget(Agent, Target)	SetTarget(Players, Target) (no arrays)
Subscription	.Subscribe(MyFunc)	Wrong event name or handler type
Progress	Channel signal or method / UEFN	Calling with invalid agent
Tips
Always confirm the event and handler signature in Verse.
If you want tracker completion to be global (not agent-specific), you need to customize logic in Verse or through device settings.
Use SetTitleText for localization and better UI.
Prefer channel-based progression when integrating with other devices without Verse.

"""}
        ),
        Document(
            page_content="Device Name: billboard_device",
            metadata={"info": """
billboard_device — Complete Device Reference
Purpose
The billboard_device displays custom, in-world floating messages to players. It’s designed for onboarding, instructions, feedback, and score keeping, and can be dynamically updated via Verse at runtime.

All Methods
Method	Signature / Description	Example
SetText(Text:message)	Sets the main display text using a localized message.	Billboard.SetText(MyMessage)
SetTextSize(Size:int)	Sets the displayed text size.\* (Range: [8, 24])	Billboard.SetTextSize(16)
SetTextColor(Color:color)	Sets the text color. Use named/colors or custom values.	Billboard.SetTextColor(NamedColors.Blue)
SetShowBorder(Show:logic)	Shows (true) or hides (false) the border around the billboard.	Billboard.SetShowBorder(true)
GetShowBorder()<transacts>:logic	Returns current border visibility state.	if (Billboard.GetShowBorder()): ...
GetTextSize()<transacts>:int	Returns current text size.	Size := Billboard.GetTextSize()
ShowText()	Displays the current text on the billboard (makes it visible).	Billboard.ShowText()
HideText()	Hides the current text (billboard remains in world, but message is invisible).	Billboard.HideText()
UpdateDisplay()	Updates device visuals per most recent settings, if changed via Verse/UI.	Billboard.UpdateDisplay()
> \* The effective visible text length also depends on size and font—UEFN limits display up to 150–512 characters visibly.

Events and Subscriptions
No custom events or subscribable events exist for billboard_device.
Cannot subscribe to interactions or trigger events from this device in Verse.
Typical Usage Pattern
Setting Text (with Localization Support):
verse
StringToMessage<localizes>(Text: string): message = "{Text}"
 
OnBegin<override>()<suspends>:void=
    Billboard.SetText(StringToMessage("Welcome to the Game!"))
    Billboard.SetTextColor(NamedColors.Yellow)
    Billboard.SetTextSize(24)
    Billboard.ShowText()

Changing Billboard Appearance:
verse
Billboard.SetShowBorder(true)
Billboard.SetTextColor(NamedColors.Aqua)
Billboard.SetTextSize(18)
Billboard.UpdateDisplay()

Hiding and Showing:
verse
Billboard.HideText()
# ...later
Billboard.ShowText()

Using in Your Device
See this example:

verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/UI }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /Verse.org/Colors }
 
billboard_example_device := class(creative_device):
 
    @editable
    MyBillboard : billboard_device = billboard_device{}
 
    StringToMessage<localizes>(Text: string): message = "{Text}"
 
    OnBegin<override>()<suspends>:void=
        MyBillboard.SetText(StringToMessage("Welcome to the Game!"))
        MyBillboard.SetTextColor(NamedColors.Yellow)
        MyBillboard.SetTextSize(32)
        MyBillboard.ShowText()

Device Properties (UEFN Details Panel - not Verse):
Text:
Message to display (up to 512 characters possible; visible range can be <150 depending on text size/font).
Show Border:
On/Off (Border/no border; disables collision if off).
Display Mode:
One-Sided or Two-Sided (Billboard text visible from one or both sides).
Text Size:
Range 8–24 (in Details and via Verse).
Text Color, Background Color:
Any named or custom color.
Justification:
Left, Center, Right.
Font, Outline, Shadow:
Options for further text style.
View Distance:
How far away text may be read (tiles/infinite).
Correct Usage (Versus Mistakes)
Rule/Aspect	Correct Example	Incorrect Example
Set text	SetText(StringToMessage("msg"))	SetText("msg") (use message not string)
Text localization	Use <localizes> message for text	Direct string assignment
Text size limits	8 ≤ N ≤ 24	SetTextSize(100) fails, clamps to [8,24]
Color assignment	Use NamedColors.* or a color value	Using invalid type
Show/Hide text	ShowText() / HideText()	-
Border visibility	SetShowBorder(true/false)	-
Subscriptions	None (cannot subscribe to events)	-
Events/Triggers	Billboard does not emit events	-
Common Mistakes & Gotchas
Event subscription: billboard_device has no events to subscribe to.
Direct strings passed to SetText: must always convert via a localized message for best-practice and internationalization.
Text too long or size too large: only a portion may display, depending on billboard size and settings.
Advanced: Dynamically Updating Billboard (e.g., Scoreboard)
verse
var Score : int = 0
 
OnSomeGameEvent():void=
    set Score += 1
    Billboard.SetText(StringToMessage("Score: {Score}"))

Summary Table
Method/Event	Usage	Returns/Action
SetText(message)	Sets visible text	none
SetTextSize(int)	Sets text size [8,24]	none
SetTextColor(color)	Sets text color	none
SetShowBorder(logic)	Shows/hides border	none
GetShowBorder()	Checks border state	logic
GetTextSize()	Returns text size	int
ShowText()	Makes text visible	none
HideText()	Hides text	none
UpdateDisplay()	Refreshes changes	none
Events	None	
Best Practices
Always use localization functions when setting messages.
Always check text size and readability—test with your longest expected string.
Billboard is display-only: cannot be interacted with, and does not emit Verse events.
Only use in contexts where player cannot interact with the display device.
"""}
        ),
    Document(
            page_content="Device Name: tracker_device ",
            metadata={"info": """
tracker_device — Full Reference
Purpose
The tracker_device is used to count player, team, or channel-driven progress toward a goal (such as collecting items, performing actions, or receiving signals). When the tracked count meets the target, it triggers its completion logic, and can interact with other devices and Verse code.

Key Methods (Verse API)
Method	Description / Signature	Example Usage
SetTarget(Agent:agent, Value:int)	Sets a custom tracked value for a player. Must be called with a valid player agent.	MyTracker.SetTarget(Player, 5)
SetTitleText(Title:message)	Sets the visible label/title for the tracker to a localized message.	MyTracker.SetTitleText(MyMessage)
IncrementProgress(Agent:agent)	Increases the tracked count for a given agent (player).	MyTracker.IncrementProgress(Player)
ResetProgress(Agent:agent)	Resets progress for the given agent.	MyTracker.ResetProgress(Player)
Enable()	Enables the tracker device.	MyTracker.Enable()
Disable()	Disables the tracker.	MyTracker.Disable()
> Note: Some tracker_device methods are for channel-based tracking set up in the UEFN Details Panel, and not directly callable in Verse.

Key Event(s)
Event Name	Handler Signature	Description	Example Subscription
CompleteEvent	Handler(agent):void	Fires when a given agent completes the tracker objective (reaches goal).	MyTracker.CompleteEvent.Subscribe(OnCompleted)
Example subscription:
verse
MyTracker.CompleteEvent.Subscribe(OnCompleted)
OnCompleted(Agent:agent):void = ... # Agent is the player who completed the tracker

Incorrect:
❌ MyTracker.CompletedEvent.Subscribe(...) — *Incorrect event name*
❌ Handler(Result: elimination_result):void — *Incorrect handler signature*
Typical Setup Example
verse
@editable
MyTracker : tracker_device = tracker_device{}
 
OnBegin<override>()<suspends>:void=
    MyTracker.CompleteEvent.Subscribe(OnTrackerCompleted)
    MyTracker.SetTitleText(StringToMessage("Collect 5 Stars"))
    if (Player := GetPlayspace().GetPlayers()[0]):
        MyTracker.SetTarget(Player, 5)
 
OnTrackerCompleted(Agent:agent):void=
    # Do something when tracker completes for this agent

Common Configuration (Device Details Panel in UEFN)
Stat to Track:
Usually set to "Channel" for signal-based progress, or to in-game actions (eliminations, collections, etc).
Target Value:
The goal (how many events to track before completion).
Reset Between Rounds:
Whether progress resets each round.
Tracker Title:
The label visible to players.
You can also wire up channels for incrementing progress or handling tracker completion if not using Verse.
Correct Event & Subscription Rules
Always use .CompleteEvent (not .CompletedEvent).
Always subscribe with a function that takes a single agent parameter.
Incorrect Usage
Subscribing with the wrong event name (.CompletedEvent, .CompeteEvent, etc.).
Handler function with the wrong parameter type (elimination_result, ?agent, or no parameters).
Passing an array of agents or other types to methods/events.
Calling progress or completion methods outside of a failure context (if required).
Interaction with Other Devices
You can trigger other devices (such as trigger_device, end_game_device, item_granter_device, etc.) upon tracker completion via Verse in the event handler, or by wiring channels in the Details panel.
Verse lets you react programmatically to tracker progress and completion, enabling more dynamic gameplay control.
Quick Example: Awarding an Item When Complete
verse
@editable
MyTracker : tracker_device = tracker_device{}
@editable
RewardTrigger : trigger_device = trigger_device{}
 
OnBegin<override>()<suspends>:void=
    MyTracker.CompleteEvent.Subscribe(OnTrackerCompleted)
 
OnTrackerCompleted(Agent:agent):void=
    RewardTrigger.Trigger(Agent)

Summary Table
What	Correct	Incorrect
Event Name	.CompleteEvent	.CompletedEvent
Handler Sig	(Agent:agent):void	(Result: elimination_result):void or anything else
SetTarget	SetTarget(Agent, Target)	SetTarget(Players, Target) (no arrays)
Subscription	.Subscribe(MyFunc)	Wrong event name or handler type
Progress	Channel signal or method / UEFN	Calling with invalid agent
Tips
Always confirm the event and handler signature in Verse.
If you want tracker completion to be global (not agent-specific), you need to customize logic in Verse or through device settings.
Use SetTitleText for localization and better UI.
Prefer channel-based progression when integrating with other devices without Verse.

"""}
        ),
        Document(
            page_content="Device Name: item_remover_device",
            metadata={"info": """
item_remover_device — Full Device Reference
Purpose
The item_remover_device is used to cause players to lose or drop items from their inventory under specific conditions—such as on elimination, on event triggers, or on action. Items can be removed, dropped, or dropped at a specific spot, with flexible options.

Device Methods (Verse API)
Method	Signature	Description	Example
Remove(Agent:agent)	Removes the configured set of items from the Agent’s inventory, following device configuration.	ItemRemover.Remove(Player)	
Enable()	Enables the item remover device.	ItemRemover.Enable()	
Disable()	Disables the device.	ItemRemover.Disable()	
Typically, only the Remove method is used in Verse scripting for actual item removal logic.
Direct Event Binding (Device Pin/Panel Connections)
Enable When Receiving From: Enable device when another device triggers an event.
Disable When Receiving From: Disable device when another device triggers an event.
Remove When Receiving From: Remove items when specific events occur on another device.
How to use:
In UEFN’s Details panel, set up direct binding so an event (such as a player elimination, trigger, button, etc.) causes one of these functions on the item remover to execute automatically.

Events
The item_remover_device does NOT emit events (not subscribable in Verse).
Instead, it responds to manual Verse calls with Remove() or to direct event binding or channel triggers.
Details Panel/Device Options Configuration
All functional options and how they affect gameplay:

Option	Values/Settings	Description
Enabled During Phase	None, All, Pre-Game Only, Gameplay Only	Controls when Remover is active.
Affected Objects	All Objects, Building Materials, World Resources, Objects in Device, Weapons and Items, Weapons, Items	Defines what can be removed.
Amount to Remove	Amount in Device, Percentage	How much to remove.
Percentage to Remove	100%, or custom percent	Shows if “Percentage” selected—the percent of items taken.
Removal Method	Remove Items, Drop Items, Drop Items On Previous Ground Location	Remove from inventory or drop to the world.
Remove All Variations of Selected Item	On/Off	If on, removes all variants/rarities of the item chosen.
Allowed Team	Any, Pick a team	Restrict who can activate/removal is applied to.
Allowed Class	No Class, Any, Pick a class	Restrict to class/no class/anyone.
Apply To	Player, Players of Team, Players of Class, All Players	Who the removal affects.
Play Audio	On/Off	Plays sound on item removal.
Item List	Selected in panel	The list of items to target for removal/drop.
Note:
Many options interact (contextual filtering)—for example, “Percentage to Remove” only shows if “Amount to Remove” is set to Percentage.
The core *which items* and *how* is set up in the Details panel, not via Verse.
Usage can be made team/class specific with these controls.
Typical Verse Usage Example
Common: Remove items from a player on event
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
 
item_removal_example := class(creative_device):
    @editable
    ItemRemover : item_remover_device = item_remover_device{}
    @editable
    MyButton : button_device = button_device{}
 
    OnBegin<override>()<suspends>:void=
        MyButton.InteractedWithEvent.Subscribe(OnButtonPressed)
 
    OnButtonPressed(Agent:agent):void=
        ItemRemover.Remove(Agent)

Here, when a button is pressed, the specified items are removed/dropped from the player who interacted.
Design Example
Make a player instantly drop all their weapons on elimination:
1. Place an item_remover_device and configure:
Affected Items: Weapons and Items
Amount to Remove: Percentage (100%)
Removal Method: Drop Items
2. Set up an elimination trigger (e.g., use Down But Not Out device or subscribe to character elimination in Verse). 3. On elimination event, call ItemRemover.Remove(Agent).
Correct Usage Rules
Only call Remove(Agent) on a valid agent (player reference).
Configure all target items/settings in the UEFN Details panel.
Use direct event binding for no-code workflows, or Verse for custom scripting.
No events can be subscribed to—the device is action-only.
Incorrect Usage / Common Mistakes
Mistake	Why it Fails/Odds Result
Calling ItemRemover.Remove() with no agent	Fails—must provide a valid agent
Trying to subscribe to events (none exist)	No events to subscribe to
Expecting to remove items not listed in options	Only items as per config will be removed
Setting conflicting teams/classes/config	Device may not apply if rules conflict
Passing arrays to Remove()	Only single agent accepted per call
Best Practices
Always test your “Affected Objects” and “Apply To” settings for expected gameplay.
When scripting with Verse, combine with triggers, buttons, or elimination events for best effect.
Use direct event binding for simple cause/effect setup in the Details panel.
Summary Table
What	Example Code / Setting	Note
Remove method	ItemRemover.Remove(Agent)	Verse call; agent required
Enable/disable	ItemRemover.Enable(), ItemRemover.Disable()	Optional via Verse
No events	—	Cannot subscribe
Setup affected items	UEFN Details Panel “Item List” option	Not Verse
Amount/Method/Rule config	All set in Details panel	Not in Verse
Direct event binding	“Remove When Receiving From” in Details	No code needed
Practical Advanced Pattern
Combining item removal and item granting in a workflow:
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
 
@editable
ItemRemover : item_remover_device = item_remover_device{}
@editable
ItemGranter : item_granter_device = item_granter_device{}
@editable
Spawner : player_spawner_device = player_spawner_device{}
 
OnBegin<override>()<suspends>:void=
    Spawner.SpawnedEvent.Subscribe(OnPlayerSpawned)
 
OnPlayerSpawned(Agent:agent):void=
    ItemRemover.Remove(Agent)
    ItemGranter.GrantItem(Agent)

Removes configured items, then grants new ones on spawn.
"""}
        ),

        Document(
            page_content="Device Name: creature_spawner_device",
            metadata={"info": """
creature_spawner_device — Complete Reference
Purpose
The creature_spawner_device spawns AI-controlled hostile creatures (e.g., Cube Fiends, Brutes, or custom enemies) in your island. It allows you to configure spawn type, quantity, timing, despawn logic, strength, location, and special features. You can control it from Verse or through other Creative devices.

Verse API Methods
Method	Signature	Description	Example
Enable()	():void	Enables the spawner. Begins spawning creatures according to settings.	Spawner.Enable()
Disable()	():void	Disables the spawner and despawns creatures (based on settings).	Spawner.Disable()
Verse Events
Event Name	Handler Signature	Description	Example Subscription
SpawnedEvent	(Agent:agent):void	Fires every time this spawner spawns a creature.	Spawner.SpawnedEvent.Subscribe(OnCreatureSpawned)
EliminatedEvent	(Result:device_ai_interaction_result):void	Fires when a spawned creature is eliminated.	Spawner.EliminatedEvent.Subscribe(OnCreatureEliminated)
Typical Usage in Verse
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Fortnite.com/AI }
 
creature_spawner_example := class(creative_device):
    @editable
    Spawner : creature_spawner_device = creature_spawner_device{}
 
    OnBegin<override>()<suspends>:void=
        Spawner.SpawnedEvent.Subscribe(OnCreatureSpawned)
        Spawner.EliminatedEvent.Subscribe(OnCreatureEliminated)
        Spawner.Enable()
 
    OnCreatureSpawned(Agent:agent):void=
        Print("Creature spawned!")
 
    OnCreatureEliminated(Result:device_ai_interaction_result):void=
        if (Source := Result.Source?):
            Print("Creature eliminated by source!")
        else:
            Print("Creature eliminated!")

Details Panel Configuration Options (Core Gameplay Settings)
Option	Common Values	Description
Spawner Type	Cube Spawner, Ice Spawner…	Visual appearance and type.
Creature Type	Fiend, Brute, Cube Random…	What enemies spawn.
Number of Creatures	integer (e.g., 1–12)	Max creatures to have active at a time.
Limit Spawned Creatures	Yes/No	Whether to limit *total* creatures spawned during device lifetime.
Total Spawn Limit	integer	Max creatures ever spawned. Shows if limit is "Yes".
Wave Timer	seconds	Min time between spawn waves.
Activation Range	tiles/meters	How close a player must get to activate sends.
Despawn Range	tiles/meters	How far creatures can wander before being despawned.
Despawn Type	Distance to Enemy/Spawner/None	What to calculate despawn from.
Invincible Spawner	On/Off	Whether the spawner can be destroyed by players.
Spawner Visibility	On/Off	Spawner visible/invisible (invisible = no collision, not targetable).
Damage Spawner After Spawn	On/Off	Spawner takes damage each time it spawns a creature.
Spawn Effects Visibility	On/Off	Visual VFX/SFX on spawn.
Damage Structures at Spawn	On/Off	Whether spawned creatures damage nearby player structures.
Max Spawn Distance	tiles/meters	How far from the spawner creatures can spawn.
Spawn Through Walls	On/Off	Whether creatures can spawn through walls/blocking geometry.
Preferred Spawn Location	At Max Distance/Random	Spawn creatures randomly or at farthest valid point.
Enabled At Game Start	On/Off	Device begins spawning at round start (if On).
Ambience Sound	On/Off	Whether the spawner plays a constant sound effect.
Restore Player Shield on Elimination	On/Off	Restore player's shield when they eliminate a spawned creature.
> Note: Many advanced settings (e.g. event-based enabling/disabling, direct event binding to buttons/timers, etc.) are controlled by connecting devices in UEFN or via Verse.

Direct Event Binding / Channel Triggers
Enable When Receiving From: Channel/event can trigger spawner to begin operation.
Disable When Receiving From: Channel/event can stop spawner and despawn creatures.
Other devices (triggers, buttons, timers, etc.) can be linked in the Details panel for non-scripting control.
Example Use Cases
Waves of Enemies: Turn spawner on/off via Verse, triggers, or game phase. Configure for escalating waves by changing device options.
Interactive Encounters: Enable spawners when a button or player reaches a zone.
Reward Logic: Upon spawner’s EliminatedEvent, grant items or open areas to players.
Correct Subscription & Usage Rules
Subscribe to SpawnedEvent with (Agent:agent):void
Subscribe to EliminatedEvent with (Result:device_ai_interaction_result):void
Call Enable()/Disable() to control spawn activation from Verse
Configure spawn limits and behavior in UEFN Details panel
Incorrect Usage Examples
Incorrect Example	Why it’s Wrong
Spawner.CompletedEvent.Subscribe(...)	No such event; correct is SpawnedEvent or EliminatedEvent
Handler with wrong type: (Result: elimination_result)	EliminatedEvent sends device_ai_interaction_result
Calling methods on null/unset device reference	Device must be set via @editable and assigned in editor
Expecting direct player control of enemies	Only Verse, device, or sequence events can control them
Best Practices
Always set correct handler signatures.
Test device settings (count/limit/range) for your gameplay design.
Use Details panel for visual and functional configuration (creature type, appearance, limits).
Use Verse methods for dynamic, script-based control.
Summary Table
What/Feature	Correct Example	Note
Enable/Disable	Spawner.Enable(), Spawner.Disable()	Verse/control device
Spawn event	.SpawnedEvent.Subscribe(MyHandler) (Agent:agent):void	Agent is creature spawned
Elimination event	.EliminatedEvent.Subscribe(MyHandler) (Result:device_ai_interaction_result):void	
Direct binding	Set “Enable/Disable When Receiving From” channel in Details	No code needed
Limits/Type	Set type/limit/count in Details Panel	Not Verse
Common Mistakes
Misspelling event names (.SpawnEvent/.EliminationEvent do not exist)
Wrong handler signatures (always match correct type)
Setting limits in Verse—must be configured in Details panel
Expecting devices to spawn custom Fortnite creatures—only supported types allowed
"""}
        ),
    Document(
            page_content="Device Name: player_spawner_device",
            metadata={"info": """
📘 player_spawner_device
Description:
The player_spawner_device controls where and how players spawn on your island. You can enable/disable spawn pads, assign to teams or classes, trigger player spawns via Verse or events, and listen for spawn events. Essential for custom multiplayer, class/team setup, and respawn rules.

📥 Imports Required:
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

🧰 Core Methods:
Method	Signature	Description
Enable	Enable(): void	Enables the spawner for use (can now spawn players).
Disable	Disable(): void	Disables this spawner (players cannot spawn here while disabled).
Register	Register(Agent:agent):void	Registers a specific player (agent) to this spawner.
Unregister	Unregister(Agent:agent):void	Unregisters a specific player (agent) from this spawner.
📣 Events (Verse Subscriptions):
Event Name	Handler Signature	Description
SpawnedEvent	(Agent:agent):void	Fires when a player spawns at this spawner.
SpawnFailedEvent*	(Agent:agent):void	*(Not always exposed; rarely used in Verse—see UEFN for details.)*
How to subscribe:
verse
Spawner.SpawnedEvent.Subscribe(OnPlayerSpawned)
OnPlayerSpawned(Player: agent):void =
    Print("Player spawned at spawner!")

🖥️ Device Panel Options (UEFN Editor):
Option	Description
Enabled During Phase	When the spawner is active: Always, None, Create Only, Game Countdown Only, Gameplay Only
Player Team	Which team is allowed to use this pad (None, Any, or specific team)
Player Class	Which class is allowed (Any, No Class, Team, or pick a class)
Priority Group	Advanced; controls order of spawn pad selection (Primary/Secondary/etc)
Use as Island Start	If on, can be used for initial player spawns
Visible in Game	Show or hide spawner mesh during play
Play Audio	Should spawner make a sound when used
Enemy Range Check	Prevents spawning if enemies are within X meters (fallback if all spawners blocked)
Display Enemy Range	Whether to show enemy check distance visual (editor only)
Respawn Alive Players	Determines if spawner force-respawns living players
🔗 Direct Event Binding (Pin/Panel Setup):
Enable When Receiving From: Enable device when another device sends a signal
Disable When Receiving From: Disable device on signal
Spawn Player When Receiving From: Spawn/respawn a player on signal from another device
On Player Spawned Send Event To: Trigger functions on other devices when a player spawns here
On Spawn Failed Send Event To: Trigger on other devices when a spawn fails at this spawner
🚦 Common Usage Example:
verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
 
player_spawner_example := class(creative_device):
 
    @editable
    Spawner : player_spawner_device = player_spawner_device{}
 
    OnBegin<override>()<suspends>: void =
        Spawner.Enable()
        Spawner.SpawnedEvent.Subscribe(OnPlayerSpawned)
 
    OnPlayerSpawned(Player: agent):void =
        Print("Player spawned at spawner!")

✅ Best Practices:
Use one spawner per intended spawn location for best control
Set team/class rules in the Details panel to force custom rules
Always subscribe to SpawnedEvent for custom spawn logic (e.g., item grants, welcome UI)
Use Enable()/Disable() to toggle pads dynamically via game logic
Use Register/Unregister for explicit player-to-pad control if needed
❌ Common Mistakes:
Not enabling the spawner if you want it used (players fall from sky instead)
Using the wrong handler signature (must be (Agent:agent):void)
Forgetting to configure team/class restrictions
Attempting to spawn via the spawner device without a proper signal or Verse logic
Summary Table
Feature	Supported / Note
Enable/Disable (Verse)	✅ via .Enable(), .Disable()
Assign to Team/Class	✅ Details panel only
Subscribe to Spawn Event	✅ via .SpawnedEvent.Subscribe(handler)
Spawn via Channel/Signal	✅ “Spawn Player When Receiving From”
Directly spawn in Verse	❌ Not supported (must register, then respawn)
No hidden events, no extra API—everything above is developer-ready.
"""}
        )
    
    

    ]
    
    print(f"  - {len(manual_documents)} documents have been defined.")

    if not manual_documents:
        print("\nThe document list is empty. Halting the process.")
        return

    # --- 3. Create and Save the FAISS Vector Store ---
    print(f"\nCreating FAISS index from {len(manual_documents)} documents...")
    
    # Ensure the target directory exists
    if not os.path.exists(PERSIST_DIRECTORY):
        os.makedirs(PERSIST_DIRECTORY)
        print(f"Created directory: '{PERSIST_DIRECTORY}'")

    # Create the FAISS index from the documents and embeddings in memory
    vector_store = FAISS.from_documents(
        documents=manual_documents,
        embedding=embeddings
    )
    
    # Save the created index to the specified local path
    vector_store.save_local(folder_path=PERSIST_DIRECTORY)

    print("\n✅ Ingestion complete!")
    print(f"FAISS vector store has been successfully created and saved at '{PERSIST_DIRECTORY}'.")

if __name__ == "__main__":
    ingest_manual_device_data_faiss()