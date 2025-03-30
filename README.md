# AppleJam

## Overview
AppleJam is a project that explores signal jamming and decoding using PlutoSDR (Software Defined Radio). The project involved designing and implementing multiple jamming techniques, including static and reactive jamming, to interfere with signals such as those used by drones and smart devices.

## Features
- **Static Jammer** (`ProgrammesAtomiques/StaticJammer.py`): Transmits broadband white noise over a wide frequency range to disrupt signals, even those using frequency hopping (observed via `ProgrammesAtomiques/spectrogramm.py`).
- **Reactive Jammer** (`ProgrammesAtomiques/reactiveJammerPrise`): Monitors a wide frequency band using `ProgrammesAtomiques/spectrogramm.py` and detects unusual signal peaks before emitting concentrated white noise on the detected frequency.
- **Signal Analysis**: Various tools and scripts were developed to analyze signals, detect modulation types, and attempt communication between PlutoSDR devices.

## Project Timeline
### February 2024
- **Initial Setup**: Team members studied PlutoSDR documentation, signal jamming techniques, and hardware specifications.
- **First Tests**: Implemented initial spectrogram analysis and started troubleshooting hardware and software compatibility issues.

### March 2024
- **Signal Reception & Identification**: Captured and analyzed signals from smart plugs and drones.
- **Development of Jamming Techniques**: Manual jamming of smart plug signals and exploration of frequency hopping in drones.
- **PlutoSDR Configuration**: Troubleshooting USB transmission rates and improving communication between Pluto devices.

### April 2024
- **Advanced Signal Analysis**: Determined modulation types for different devices (e.g., FSK for drones).
- **First Functional Jamming**: Successfully jammed a smart plug using the reactive jammer.
- **Attempted Communication**: Developed AM/FM/QPSK transmission scripts but faced significant errors in signal reproduction.

### May - June 2024
- **Spectrogram Refinement**: Improved visualization and debugging of emitted/received signals.
- **Final Testing & Evaluation**: Reactive jamming applied to a drone, though attempts to block a specific frequency were unsuccessful.
- **Project Completion**: Finalized documentation, presented findings, and summarized results.

## Challenges & Learnings
- **Hardware Limitations**: Weak transmission power from PlutoSDR made jamming difficult.
- **Interference Issues**: External signals often disrupted experiments, requiring adjustments in frequency selection.
- **Software & Compatibility Problems**: Frequent troubleshooting was needed for OS compatibility, library installations, and VM issues.
- **Signal Reconstruction**: Successfully jamming signals was easier than reproducing them accurately.

## Future Improvements
- Enhancing the transmission power of PlutoSDR.
- Refining the reactive jammer to dynamically adapt to more complex frequency-hopping signals.
- Improving signal decoding and reconstruction for practical applications.

## Contributors
- **Paul Archer**: Signal analysis, troubleshooting, and PlutoSDR scripting.
- **Amine Medjahed**: PlutoSDR configuration, scripting, and debugging.
- **Maëliss De Baumont**: Research on jamming techniques and documentation.
- **Alexander Hare**: Spectrogram analysis, modulation identification, and jamming implementation.
- **Thomas**: Signal modeling, simulation, and algorithm optimization.

## Resources
- [PlutoSDR GitHub](https://github.com/jorgejc2/PlutoSDR/tree/master) - Spectrogram tool
- [Live Frequency Analysis](https://github.com/r4d10n/retrogram-plutosdr) - Real-time PlutoSDR visualization

## License
This project is for educational and research purposes only. Unauthorized signal interference may be illegal in some jurisdictions. Use responsibly.

---
For more details, refer to the project's internal documentation and progress reports.

