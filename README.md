# Python Scripting in Blender

WIP ( Work in Progress ).  
블렌더를 위한 애드온 개발을 위해서 생성 하였습니다.  

- VS Code의 명령창(Ctrl+Shift+P)에서 'Blender: Run Script'로 실행시에는 __name__ 이 "<run_path>" 로 설정되어 코드 수정 필요 ...  
- ...  



## 책 관련 링크

<img src="https://content.packt.com/B18375/cover_image.png" alt="" height="256px" align="right">

- [Python Scripting in Blender [ 원서 ]](https://www.packtpub.com/en-us/product/python-scripting-in-blender-9781803234229)  

- [Source Code](https://github.com/PacktPublishing/Python-Scripting-in-Blender)  


## 개발 및 테스트 환경

- 시스템 ( Computer System )  

  - AMD Ryzen 9 5900X 12-Core Processor
  - 32G RAM
  - NVIDIA Geforce RTX 3080 10GB
  - SSD 2TB
  - Windows 11 64bit Korean

- 블렌더 ( Blender 4.4.3 )  

  - [Blender Download](https://www.blender.org/download/)  
    - [v4.4.3 for Windows](https://download.blender.org/release/Blender4.4/blender-4.4.3-windows-x64.msi)  
    - [v4.4.0 for Windows](https://download.blender.org/release/Blender4.4/blender-4.4.0-windows-x64.msi)  
    - 내장된 파이썬 버전은 Python v3.11.11 입니다.  

- 파이썬 ( Python 3.12 )  

  - [Python Download](https://www.python.org/downloads/)  
    - [v3.12.0 for Windows](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)  
    - [v3.11.9 for Windows](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)  

- 에디터 ( Editor, Intergrated Development Environment )  

  - [VS Code](https://visualstudio.microsoft.com/ko/free-developer-offers/)  
    - [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
      - Python Interpreter Chooser  
      - Pylance  
      - Python Debugger  
      -  
    - [Blender Development](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development)  
      - Blender: Start  
      - Blender: Stop  
      - Blender: Run Script  
      -  

- 패키지 매니저 ( Package Manager )
  - [pypi](https://pypi.org/)  
    - [검색](https://pypi.org/search/)  
    - ...
    ```
    $ pip --version
    $ pip --help
    ```
    ```
    $ pip install fake-bpy-module-latest
    $ pip list
    ```
    ```
    $ pip freeze >> requirements.txt
    $ pip install -r ./requirements.txt
    ```


## 사용된 패키지 목록

- fake-bpy-module
  - [pypi](https://pypi.org/project/fake-bpy-module/)  
    ```
    $ pip install fake-bpy-module-latest
    ```
  - [fake-bpy-module](https://github.com/nutti/fake-bpy-module)  
  - Fake Blender Python API module collection

- ...
  - [pypi]()  
  ```
  $ vcpkg add port ...
  ```
  - [...]()
  - ...  


## ...

---  
---  
---  






# Python-Scripting-in-Blender

<a href="https://www.packtpub.com/product/python-scripting-in-blender-3x/9781803234229?utm_source=github&utm_medium=repository&utm_campaign=9781803235851"><img src="https://content.packt.com/B18375/cover_image_small.png" alt="" height="256px" align="right"></a>

This is the code repository for [Python Scripting in Blender](https://www.packtpub.com/product/python-scripting-in-blender-3x/9781803234229?utm_source=github&utm_medium=repository&utm_campaign=9781803235851), published by Packt.

**Extend the power of Blender using Python to create objects, animations, and effective add-ons**

## What is this book about?
Blender, a powerful open source 3D software, can be extended and powered up using the Python programming language. This book teaches you how to automate laborious operations using scripts, and expand the set of available commands, graphic interfaces, tools, and event responses, which will enable you to add custom features to meet your needs and bring your creative ideas to life.

This book covers the following exciting features:                                 
* Understand the principles of 3D and programming, and learn how they operate in Blender
* Build engaging and navigation-friendly user interfaces that integrate with the native look and feel
* Respect coding guidelines and deliver readable and compliant code without the loss of originality
* Package your extensions into a complete add-on, ready for installation and distribution
* Create interactive tools with a direct response to the user's action
* Code comfortably and safely using version control

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1803234229) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
bl_info = {
    "name": "Object Shaker",
    "author": "Packt Man",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "description": "Add Shaky motion to active object",
    "location": "Object Right Click -> Add Object Shake",
    "category": "Learning",
}
```

**Following is what you need for this book:**
This book is for Blender users who want to expand their skills and learn scripting, technical directors looking to automate laborious tasks, and professionals and hobbyists who want to learn more about the Python architecture underlying the Blender interface. Prior experience with Blender is a prerequisite, along with a basic understanding of the Python syntax—however, the book does provide quick explanations to bridge potential gaps in your background knowledge.

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-12 | Blender 3.3 | Windows, Mac OS X, and Linux (Any) |
| 1-12 | Visual Studio Code 1.70 or later | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/G1mMt).

### Related products
* Blender 3D Incredible Models [[Packt]](https://www.packtpub.com/product/blender-3d-incredible-models/9781801817813?utm_source=github&utm_medium=repository&utm_campaign=9781801817813) [[Amazon]](https://www.amazon.com/dp/B0B1QMV8LR)

* Squeaky Clean Topology in Blender [[Packt]](https://www.packtpub.com/product/squeaky-clean-topology-in-blender/9781803244082?utm_source=github&utm_medium=repository&utm_campaign=9781803244082) [[Amazon]](https://www.amazon.com/dp/1803244089)

## Errata 
 * Page 45 (second last code block):
``` 
import bpy
for ob in bpy.context.selected_objects:
ob.select_set(False)
```
**_should be_**
``` 
 import bpy
 for ob in bpy.context.selected_objects:
     ob.select_set(False)
 ```

## Get to Know the Author
**Paolo Acampora** is a software developer at Binary Alchemy and a veteran technical director for animation, visual effects, and prototyping. He is a long-time Blender user and advocates for the widespread adoption of open source software and code literacy.
He works with studios to kickstart their computer graphics pipelines and shares his tools with the Blender community.
