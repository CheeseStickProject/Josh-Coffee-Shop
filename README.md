# Coffee Empire Idle Game

Coffee Empire is an engaging idle/incremental game built with Python and Tkinter. Start from humble beginnings and build your coffee empire from scratch!

## Features
- **Interactive Coffee Brewing**: Click to brew coffee and earn money with satisfying visual feedback
- **Automated Production**: Hire various producers to automate your coffee empire:
  - Baristas - Your first employees
  - Coffee Machines - Automate the brewing process
  - Coffee Shops - Expand your retail presence
  - Coffee Farmers - Control your supply chain
  - Coffee Factories - Mass production capabilities
  - Global Franchises - Ultimate expansion
- **Strategic Upgrades**: Purchase powerful upgrades to boost efficiency:
  - Stronger Hands - Increase click power
  - Turbo Brewing - Triple click efficiency
  - Better Beans - Enhance barista production
  - Cold Brew - Advanced brewing techniques
- **Achievement System**: Unlock achievements as you progress through your coffee journey
- **Polished UI**: Animated floating text, tooltips, and intuitive tabbed interface
- **Professional Graphics**: Custom PNG graphics for all game elements
- **Persistent Progress**: Dual save system with both JSON and SQLite database support
- **Real-time Statistics**: Track your progress with detailed stats and production rates

## Getting Started

### Prerequisites
- Python 3.x
- Tkinter (included with most Python installations)
- SQLite3 (included with Python)

### Installation & Setup
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/pf25-coffee-empire.git
   cd pf25-coffee-empire
   ```
2. Ensure all PNG image files are in the project directory
3. Run the game:
   ```bash
   python game.py
   ```

### First Time Setup
- The game will automatically create necessary database files
- Your progress is saved automatically when you close the game
- No additional installation or setup required!

### How to Play
- **Main Screen**: Click the coffee cup to brew coffee and earn money
- **Producers Tab**: Hire staff and buy equipment to automate coffee production
  - Start with Baristas for basic automation
  - Progress through Machines, Shops, Farmers, Factories, and Global Franchises
  - Each producer type offers exponentially increasing production rates
- **Upgrades Tab**: Purchase powerful upgrades to boost your efficiency
  - Click power multipliers for more money per click
  - Producer-specific multipliers for enhanced automation
  - Unlock condition-based upgrades as you progress
- **Stats & Achievements Tab**: Track your empire's growth and unlock achievements
  - Monitor total clicks, upgrades purchased, and cups brewed
  - Complete achievement challenges for bonus satisfaction

## Project Structure
```
pf25-coffee-empire/
├── game.py                    # Main game logic and UI
├── DatabaseManager.py         # SQLite database management
├── README.md                  # Project documentation
├── Graphics/                  # Game assets
│   ├── barista.png           # Barista producer icon  
│   ├── beans.png             # Coffee beans upgrade icon
│   ├── branding.png          # Branding elements
│   ├── cold_brew.png         # Cold brew upgrade icon
│   ├── cup.png               # Main brewing button
│   ├── espresso.png          # Espresso graphics
│   ├── farmer.png            # Coffee farmer icon
│   ├── hands.png/hands2.png  # Hand upgrade icons
│   ├── machine.png           # Coffee machine icon
│   ├── shop.png              # Coffee shop icon
│   ├── turbo.png/turbo2.png  # Turbo upgrade icons
├── Save Files/               # Auto-generated
│   ├── coffee_empire_save.json # JSON save format
│   └── coffee.db             # SQLite database save
```

## Game Mechanics

### Producers & Scaling
- **Exponential Growth**: Each producer type offers significantly higher production than the previous
- **Cost Scaling**: Producer costs increase by 15% with each purchase, creating strategic decisions
- **Unlock Progression**: Advanced producers unlock as you build your empire

### Upgrade System
- **Click Multipliers**: Boost your manual brewing efficiency
- **Producer Multipliers**: Enhance specific producer types
- **Conditional Unlocks**: Upgrades unlock based on your progress milestones

### Achievement System
- **First Brew**: Complete your first manual brew
- **Apprentice Barista**: Hire 10 baristas
- **Bean Tycoon**: Brew 1,000 cups total
- **Upgrade Enthusiast**: Purchase 3 upgrades

## Save System
The game features a robust dual-save system:
- **JSON Save**: `coffee_empire_save.json` for quick saves and portability
- **SQLite Database**: `coffee.db` for advanced save management and data integrity
- **Auto-Save**: Progress automatically saves when you close the game
- **Auto-Load**: Progress restores seamlessly when you restart

## Technical Details

### Built With
- **Python 3.x** - Core game engine
- **Tkinter** - GUI framework for cross-platform compatibility
- **SQLite3** - Embedded database for save management
- **JSON** - Lightweight save format option

### Key Features
- **Object-Oriented Design**: Clean, maintainable code structure
- **Database Integration**: Professional-grade save system with CRUD operations
- **Responsive UI**: Real-time updates with smooth animations
- **Scalable Architecture**: Easy to extend with new producers and upgrades

## Development

### Adding New Features
- **Producers**: Add entries to the `producers` dictionary in `game.py`
- **Upgrades**: Extend the `upgrades` dictionary with new enhancement options
- **Achievements**: Add conditions to the `check_achievements()` function
- **Graphics**: Drop PNG files in the main directory and reference in the code

### Database Schema
The SQLite database stores:
- Player statistics (cups, money, clicks)
- Producer quantities and multipliers
- Upgrade purchase states
- Achievement progress

## Credits
This project was created and developed by:
- **SethK9102**
- **Dhinman278**
- **CarsonV8824**
- **sreno77**

The music and images are from the people working on Cheese Stick

## License
This project is available for educational and personal use.
