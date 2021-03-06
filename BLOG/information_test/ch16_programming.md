## 프로그래밍 언어 활용

### 데이터 타입

1. 데이터 타입
2. C/C++의 데이터 타입 및 기억 범위
   - char
   - unsigned char
   - short
   - int
   - long
   - long long
   - float
   - double
   - long double
3. JAVA의 데이터 타입 크기 및 기업 범위
   - char
   - byte
   - short
   - int
   - long
   - float
   - double
   - boolean

### 변수

1. 변수의 개요
   - 변수는 컴퓨터가 명령을 처리하는 도중 발생하는 값을 저장하기 위한 공간으로, 변할 수 있는 값을 의미한다.
2. 변수명 작성 규칙
   - 첫 글자 숫자 안됨
   - 특수 문자 안됨
   - 예약어 사용 지양
3. 기억 클래스
   - 변수 선언 시 메모리 내에 변수의 값을 저장하기 위한 기억영역이 할당되는데, 할당 되는 기억영역에 따라 사용 범위에 제한이 있다. 이러한 기억 영역을 결정하는 작업을 기억 클래스라고 한다.
   - auto : 자동 변수는 함수나 코드의 범위를 한정하는 블록 내에서 선언되는 변수이다.
   - register : 레지스터 변수는 메모리가 아닌 CPU 내부의 레지스터에 기억영역을 할당받는 변수이다.
   - static : 정적 변수는 함수나 블록 내에서 선언하는 내부 정적 변수와 함수 외부에서 선언하는 외부 정적 변수가 있다.
   - extern : 외부 변수는 현재 파일이나 다른 파일에서 선언된 변수나 함수를 참조하기 위한 변수이다.
4. 변수의 선언

### 연산자

1. 산술 연산자
2. 관계 연산자
   - 관계 연산자는 두 수의 관계를 비교하여 참 또는 거짓을 결과로 얻는 연산자이다.
3. 비트 연산자
   - 비트 연산자는 비트별로 연산하여 결과를 얻는 연산자이다.
4. 논리 연산자
   - 논리 연산자는 두 개의 논리 값을 연산하여 참 또는 거짓을 결과로 얻는 연산자이다. 관계 연산자와 마찬가지로 거짓은 0, 참은 1이다.
5. 대입 연산자
   - 연산 후 결과를 대입하는 연산식을 간략하게 입력할 수 있도록 대입 연산자를 제공한다.
6. 조건 연산자
   - 조건 연산자는 조건에 따라 서로 다른 수식을 수행한다.
7. 기타 연산자
   - sizeof, ",", 자료형
8. 연산자 우선 순위
   - 단항 연산자
   - 이항 연산자
     - 산술 연산자
     - 시프트 연산자
     - 관계 연산자
     - 비트 연산자
     - 논리 연산자
   - 삼항 연산자
     - 조건 연산자
   - 대입 연산자
     - 대입 연산자
   - 순서 연산자
     - 순서 연산자

### 제어문

1. 제어문의 개념
   - 컴퓨터 프로그램은 명령어가 서술된 순서에 따라 무조건 위에서 아래로 실행되는데, 조건을 지정해서 진행 순서를 변경할 수 있다. 이렇게 프로그램의 순서를 변경할 때 사용하는 명령문을 제어문이라고 한다.
2. 단순 if 문
3. 다중 if 문
4. Switch문
5. goto문

### 반복문

1. 반복문의 개요
   - 반복문은 제어문의 한 종류로 일정한 횟수를 반복하는 명령문을 말한다. 보통 변수의 값을 일정하게 증가시키면서 정해진 수가 될 때까지 명령이나 명령 그룹을 반복 수행한다.
2. for 문
3. while 문
4. do~while 문
5. break, continue 문

### 배열과 문자열

1. 배열의 개념
2. 1차원 배열
3. 2차원 배열
4. 배열의 초기화
5. 배열 형태의 문자열 변수

### 포인터

1. 포인터와 포인터 변수
   - 포인터는 변수의 주소를 말하며, C언어에서는 주소를 제어할 수 있는 기능을 제공한다.
2. 포인터와 배열
   - 배열을 포인터 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있다.

### 절차적 프로그래밍 언어

1. 절차적 프로그래밍 언어의 개요
   - 절차적 프로그래밍 언어는 일련의 처리 절차를 정해진 문법에 따라 순서대로 기술해나가는 언어이다.
2. 절차적 프로그래밍 언어의 장,단점
   - 컴퓨터의 처리 구조와 유사하여 실행 속도가 빠르다.
   - 같은 코드를 복사하지 않고 다른 위치에서 호출하여 사용할 수 있다.
   - 모듈 구성이 용이하며, 구조적인 프로그래밍이 가능하다.
   - 프로그램을 분석하기 어렵다.
   - 유지 보수나 코드의 수정이 어렵다
3. 절차적 프로그래밍 언어의 종류
   - C, ALGOL, COBOL, FORTRAN

### 객체지향 프로그래밍 언어

1. 객체지향 프로그래밍 언어의 개요
   - 객체지향 프로그래밍 언어는 현실 세계의 개체를 기계의 부품처럼 하나의 객체로 만들어, 기계적인 부품들을 조립하여 제품을 만들 듯이 소프트웨어를 개발할 때도 객체들을 조립해서 프로그램을 작설할 수 잇도록 한 프로그래밍 기법이다.
2. 객체지향 프로그래밍 언어의 장 담점
   - 상속을 통한 재사용과 시스템의 확장이 용이하다.
   - 코드의 재활용성이 높다.
   - 자연적인 모델링에 의해 분석과 설계를 쉽고 효율적으로 할 수 있다.
   - 사용자와 개발자 사이의 이해를 쉽게 해준다.
   - 대형 프로그램의 작성이 용이하다.
   - 소프트웨어 개발 및 유지보수가 용이하다.
   - 프로그래밍 구현을 지원해 주는 정형화된 분석 및 설계 방법이 없다.
   - 구현 시 처리 시간이 지연된다.
3. 객체지향 프로그래밍 언어의 종유
   - 자바, C++, Smalltalk
4. 객체지향 프로그래밍 언어의 구성 요소
   - 객체지향 프로그래밍 언어의 구성 요소에는 객체, 클래스, 메시지가 있다.
5. 객체지향 프로그래밍 언어의 특징
   - 객체지향 프로그래밍 언어의 특징에는 캡슐화, 정보 은닉, 추상화, 상속성, 다형성 등이 있다.
   - 캡슐화 : 데이터와 데이터를 처리하는 함수를 하나로 묶는 것을 의미한다, 캡슐화된 객체의 세부 내용이 외부에 은폐되어 변경을 발생할 때 오류의 파급 효과가 적다.
   - 정보 은닉 : 캡슐화에서 가장 중요한 개념으로 다른 객체에게 자신의 정보를 숨기고 자신의 연산만을 통하여 접근을 허용하는 것이다.
   - 추상화 : 불필요한 부분을 생략하고 객체의 속성 중 가장 중요한 것에만 중점을 두어 개략화하는 것, 즉 모델화하는 것이다.
   - 상속성 : 이미 정의된 상위 클래스의 모든 속성과 연산을 하위 클래스가 물려받는 것이다, 상속성을 이용하면 하위 클래스는 상위 클래스의 모든 속성과 연산을 자신의 클래스 내에서 다시 정의하지 않고서도 즉시 자신의 속송으로 사용할 수 있다.
   - 다형성 : 메시지에 의해 객체가 연산을 수행하게 될 때 하나의 메시지에 대해 각 객체가 가지고 있는 고유한 방법으로 응답할 수 있는 능력을 의미한다.

### 스크립트 언어

1. 스크립트 언어의 개요
   - 스크립트 언어는 HTML 문서 안에 직접 프로그래밍 언어를 삽입하여 사용하는것으로, 기계어로 컴파일 되지 않고 별도의 번역기가 소스를 분석하여 3동작하게 하는 언어이다.
2. 스크립트 언어의 장 단점
   - 컴파일 없이 바로 실행되므로 결과를 바로 확인할 수 있다.
   - 배우고 코딩하기 쉽다.
   - 개발 시간이 짧다
   - 소스 코드를 쉽고 빠르게 수정할 수 있다.
   - 코드를 읽고 해석해야 하므로 실행 속도가 느리다.
   - 런타임 오류가 많이 발생한다.
3. 스크립트 언어의 종류
   - 자바 스크립트
   - ASP
   - JSP
   - PHP
   - Python

### 선언형 언어

1. 선언형 언어
   - 선언형 언어는 명령형 언어와 반대되는 개념의 언어로, 명령형 언어가 문제를 해결하기 위한 방법을 기술한다면 선언형 언어는 프로그램이 수행해야 문제를 기술하는 언어이다.
2. 선언형 언어의 장단점
   - 가독성이나 재사용성이 좋다.
   - 작동 순서를 구체적으로 작성하지 않기 때문에 오류가 적다.
   - 프로그램 동작을 변경하지 않고도 관련 값을 바꿀 수 있다.
3. 선언형 프로그래밍 언어 종류
   - HTML
   - LISP
   - PROLOG
   - XML
   - Haskell

### 라이브러리

1. 라이브러리의 개념
   - 라이브러리는 프로그램을 효율적으로 개발할 수 있도록 자주 사용하는 함수나 데이터들을 미리 만들어 모아 놓은 집합체이다.
     - 자주 사용하는 함수들의 반복적인 코드 작성을 피하기 위해 미리 만들어 놓은 것으로, 필요할 때는 언제든지 호출하여 사용할 수 있다.
     - 라이브러리에는 표준 라이브러리와 외부 라이브러리가 있다.
   - 표준 라이브러리 : 프로그래밍 언어에 기본적으로 포함되어 있는 라이브러리로, 여러 종류의 모듈이나 패키지 형태이다.
   - 외부 라이브러리 : 개발자들이 필요한 기능들을 만들어 인터넷 등에 공유해 놓은 것으로, 외부 라이브러리를 다운받아 설치한 후 사용한다.
2. C언어의 대표적인 표준 라이브러리
   - C언어는 라이브러리를 헤더 파일로 제공하는데, 각 헤더 파일에는 응용 프로그램 개발에 필요한 함수들이 정리되어 있다.
     - stdio.h
     - math.h
     - strign.h
     - stdlib.h
     - time.h
3. Java의 대표적인 표준 라이브러리
   - JAVA는 라이브러리를 패키지에 포함하여 제공하는데, 각 패키지에는 JAVA응용 프로그램 개발에 필요한 메소드들이 클래스로 정리되어 있다.
     - java.lang
     - java.util
     - java.io
     - java.net
     - java.awt

### 데이터 입 출력

1. C언어의 표준 입출력 함수의 개요
   - 표준 입출력 함수란 키보드로 입력받아 화면으로 출력할 때 사용하는 함수로, 대표적으로 scanf, getchar, printf, putchar, puts 등이 있다.
2. scanf 함수
3. printf 함수
4. 기타 표준 입,출력 함수
   - getchar()
   - gets()
   - putchar()
   - puts()

### 예외 처리

1. 예외 처리의 개요
   - 프로그램의 정상적인 실행을 방해하는 조건이나 상태를 예외라고 하며, 이러한 예외가 발생했을 때 프로그래머가 해당 문제에 대비해 작서앻 높은 처리 루틴을 수행하도록 하는것을 예외 처리라고 한다.
2. JACA의 예외 처리
   - JAVA는 예외를 객체로 취급하며, 예외와 관련된 클래스를 java.lang 패키지에서 제공한다.
     - try~catch문을 활용해서 처리
3. JAVA의 주요 예외 객체
   - ClassNotFoundException
   - NoSuchMethodException
   - FileNotFoundException
   - InterruptedIOException
   - ArithmeticException
   - IllegalArgumentException
   - NumberFormalException
   - ArrayIndexOutofBoundsException
   - NegativeArraySizeException
   - NullPointerException

### 프로토타입

1. 프로토타입의 개념
   - 프로그래밍 언어에서 프로토타입이란 함수 원형이라는 의미로, 컴파일러에게 사용될 함수에 대한 정보를 미리 알리는 것이다.
     - 함수가 호출되기 전에 함수가 미리 정의되는 경우에는 프로토타입을 정의하지 않아도 된다.
     - 프로토타입은 본문인 없다는 점을 제외하고 함수 정의와 형태가 동일하다.
     - 프로토타입에 정의된 반환 형식은 함수 정의에 지정된 반환 형식과 반드시 일치해야한다.
2. C언어에서의 프로토타입 선언
