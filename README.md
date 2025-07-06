# SPEECH-RECOGNITION-SYSTEM

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : KUMILI VINESH

*INTERN ID* : CITSOD647

*DOMAIN* : ARTIFICIAL INTELLIGENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

The Speech Recognizing System is a Python-based project that utilizes speech-to-text technology to convert spoken language into written text in real-time. This application is built using the speech_recognition library, one of the most popular Python libraries for implementing voice recognition functionalities. The core functionality of this system revolves around capturing audio input from the user through a microphone, processing the input using a speech recognition engine—in this case, Google’s Web Speech API—and then displaying the recognized text on the screen. This system operates in a continuous loop, actively listening for user input and converting any detected speech into textual data, making it suitable for applications like voice-controlled interfaces, transcription services, and accessibility tools for users with physical impairments.

The primary tool used in the development of this project is the speech_recognition library in Python. This library provides a simple and flexible interface for various speech recognition engines and APIs, including Google Speech Recognition, Sphinx, IBM, and others. For this specific project, Google's Web Speech API is used because of its high accuracy and ease of integration. The library is responsible for capturing the audio, handling noise, and sending it to the recognition engine for processing. It also provides helpful exception handling for various types of errors such as UnknownValueError when the speech cannot be understood, or RequestError when there is a network issue or the API is unavailable.

Another key component of the system is the Python programming language itself. Python is known for its simplicity and readability, making it an ideal choice for developing rapid prototypes and proof-of-concept applications such as this speech recognition system. The built-in support for exception handling, as well as the rich ecosystem of libraries and tools, makes Python a powerful language for implementing voice-based applications. In addition to Python, the system makes use of the pyaudio package, which is essential for accessing and managing audio streams from the microphone. pyaudio acts as the interface between the microphone hardware and the speech recognition software.

The development environment used for this project is Visual Studio Code (VS Code), a popular source-code editor developed by Microsoft. VS Code provides a lightweight, yet powerful development platform equipped with features such as syntax highlighting, debugging tools, integrated terminal, and support for Python extensions. Its simplicity and rich plugin ecosystem make it a preferred choice for Python developers. The Python extension in VS Code supports linting, IntelliSense, code navigation, and automatic formatting, which significantly enhances the development experience.

During the development process, various testing and debugging steps were carried out using VS Code’s integrated terminal and debugger to ensure the system responds appropriately to valid speech input as well as gracefully handles errors such as silence, background noise, or unclear speech. The speech recognition functionality was tested in different ambient conditions to improve its reliability, and adjust_for_ambient_noise() was employed to help the system adapt to different background noise levels.

In conclusion, the Speech Recognizing System demonstrates the power and flexibility of combining Python with the speech recognition library to build a real-time voice-to-text converter. The project showcases how modern APIs and development tools like VS Code can be leveraged to create interactive and intelligent applications with minimal setup. This system serves as a foundational project for more advanced voice-based applications, including voice assistants, smart home controls, and transcription tools.

*output :*
<img width="1440" height="900" alt="Image" src="https://github.com/user-attachments/assets/978f3abc-3c5c-4184-8d15-3389c22ec1dd" />
