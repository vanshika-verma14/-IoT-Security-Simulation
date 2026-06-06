# 🛡️ IoT Security Simulation

A comprehensive web application for simulating and monitoring security threats in IoT networks. This project demonstrates various attack scenarios and security defense mechanisms in a controlled environment.

## 🌟 Features

- **IoT Device Simulation**: Monitor multiple IoT devices (Camera, Thermostat, Door Lock, Light)
- **Attack Simulation**: Launch different types of cyber attacks (DDoS, Spoofing, Replay)
- **Security Controls**: Toggle firewall and anomaly detection systems
- **Real-time Monitoring**: Track device status and security events
- **Beautiful UI**: Modern, responsive interface with colorful design
- **Attack Logging**: Detailed logs of all security events

## 🏗️ Architecture

```
iot-security-simulation/
├── backend/                 # Python Flask API
│   ├── main.py             # Main server with IoT simulation
│   └── requirements.txt    # Python dependencies
└── frontend/               # React.js frontend
    ├── package.json        # Node.js dependencies
    ├── public/             # Static files
    └── src/                # React components
        ├── App.js          # Main application component
        ├── App.css         # Styling
        └── index.js        # Entry point
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+**
- **Node.js 14+**
- **npm** (comes with Node.js)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/iot-security-simulation.git
   cd iot-security-simulation
   ```

2. **Set up the Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   python main.py
   ```
   The backend will run on `http://localhost:5000`

3. **Set up the Frontend** (in a new terminal)
   ```bash
   cd frontend
   npm install
   npm start
   ```
   The frontend will run on `http://localhost:3000`

4. **Open your browser** and navigate to `http://localhost:3000`

## 🎮 How to Use

### 1. **Monitor IoT Devices**
- View the status of all connected IoT devices
- See real-time device status (Online/Compromised)
- Monitor device IDs and types

### 2. **Configure Security Controls**
- **Firewall**: Toggle to block DDoS attacks
- **Anomaly Detection**: Toggle to detect suspicious behavior
- View security status indicators

### 3. **Simulate Attacks**
- Select an attack type (DDoS, Spoofing, Replay)
- Choose a target device
- Launch the attack and observe the results

### 4. **Review Security Logs**
- Monitor attack attempts in real-time
- See which attacks were blocked, detected, or succeeded
- Track security event history

## 🔧 Technical Details

### Backend (Flask)
- **Framework**: Flask with CORS support
- **API Endpoints**:
  - `GET /api/devices` - Get all IoT devices
  - `GET /api/security` - Get security status
  - `GET /api/attacks` - Get available attack types
  - `POST /api/attack` - Launch an attack
  - `POST /api/security/toggle` - Toggle security controls

### Frontend (React)
- **Framework**: React 18 with hooks
- **Styling**: Custom CSS with gradients and animations
- **Features**: Responsive design, real-time updates

### Security Simulation
- **DDoS Attacks**: Blocked by firewall when enabled
- **Spoofing Attacks**: Detected by anomaly detection
- **Replay Attacks**: Detected by anomaly detection
- **Device Compromise**: Simulated when attacks succeed

## 🎨 UI Features

- **Gradient Backgrounds**: Beautiful purple-blue gradients
- **Glassmorphism Effects**: Modern glass-like card designs
- **Animated Elements**: Smooth transitions and hover effects
- **Color-coded Status**: Visual indicators for device and security status
- **Responsive Design**: Works on desktop and mobile devices

## 🔒 Security Features Demonstrated

1. **Firewall Protection**
   - Blocks DDoS attacks
   - Rate limiting simulation
   - Network traffic filtering

2. **Anomaly Detection**
   - Detects spoofing attempts
   - Identifies replay attacks
   - Behavioral analysis simulation

3. **Real-time Monitoring**
   - Device status tracking
   - Attack attempt logging
   - Security event correlation

## 📱 Screenshots

*[Add screenshots of your application here]*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Flask framework for the backend
- React.js for the frontend
- Modern CSS techniques for beautiful UI
- IoT security concepts and best practices
