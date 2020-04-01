jQuery에는 '선택'과 '동작'이 있고, '선택'을 위한 방법으로 **CSS 선택자**를 알아보았습니다. 하지만 이 외에도 **jQuery에서 제공하는 '선택' 방법**이 있습니다. 이 부분을 한번 알아봅시다.



### filter



```
$('button').filter('.color-3').text('SELECTED!');
```



`filter()`는 `()`안의 조건으로 선택된 요소를 한번 더 **걸러줍니다.** 위 코드의 경우, 모든 `button` 태그들 중에 `color-3`라는 클래스를 가지고 있는 요소만 추려내서 `text`를 바꿔주라는 의미입니다.



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 `filter`없이 모든 요소에 `text`가 적용되었고, `box-2`에서는 `filter`를 한 번 거친 후 `text`가 적용되었습니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1 button').text('SELECTED!');
    $('#box-2 button').filter('.color-3').text('SELECTED!');
  </script>
</body>
</html>
```



### not



```
$('button').not('.color-3').text('SELECTED!');
```



`not()`은 `filter()`의 반대입니다. 선택된 요소 중에서 조건에 해당되는 것들을 **제외**시킵니다. 위 코드의 경우, 모든 `button` 태그들 중에 `color-3`라는 클래스를 가지고 있는 요소만 제외하고 `text`를 바꿔주라는 의미입니다.



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 `not`없이 모든 요소에 `text`가 적용되었고, `box-2`에서는 `not`을 한 번 거친 후 `text`가 적용되었습니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1 button').text('SELECTED!');
    $('#box-2 button').not('.color-3').text('SELECTED!');
  </script>
</body>
</html>
```



### eq



```
$('button').eq(1).text('SELECTED!');
```



`eq()`는 선택된 요소들 중에서 **n번째 요소** 하나만 골라냅니다. 위 코드는 모든 `button` 태그들 중에 두 번째 요소만 골라서 `text`를 바꿔주라는 의미입니다. `eq()`안에 들어가는 숫자는 `0`부터 시작하기 때문에, `1`일 경우 두 번째 요소라는 점에 유의하세요!



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 선택된 모든 요소에 `text`가 적용되었고, `box-2`에서는 선택된 요소 중 두 번째 요소에만 `text`가 적용되었습니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1 button').text('SELECTED!');
    $('#box-2 button').eq(1).text('SELECTED!');
  </script>
</body>
</html>
```



### parent



```
$('#btn-1').parent().css('background-color', 'black');
```



`parent()`는 **부모 요소**를 찾아줍니다. 위 코드의 경우, `btn-1`의 부모 요소에 `css`를 적용해줍니다.



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 `.color-1` 자기 자신에 `css`가 적용되었고, `box-2`에서는 `.color-1`의 부모 요소에 `css`가 적용되었습니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1 .color-1').css('background-color', 'black');
    $('#box-2 .color-1').parent().css('background-color', 'black');
  </script>
</body>
</html>
```



### children



```
$('#box-1').children().css('background-color', 'black');
```



`children()`은 `parent()`의 반대입니다. 선택된 요소의 **자녀 요소**를 모두 골라줍니다.  위 코드의 경우, `box-1`의 모든 자녀 요소에 css를 적용해줍니다. `()` 안에 조건을 넣을 경우, `filter`역할도 함께 해줍니다.



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 box 자체에 `css`가 적용되었고, `box-2`에서는 box의 자식 요소들에 `css`가 적용되었습니다. `box-3`에서는 특정 조건에 맞는 자식 요소에만 `css`가 적용됩니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-3">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1').css('background-color', 'black');
    $('#box-2').children().css('background-color', 'black');
    $('#box-3').children('.color-2').css('background-color', 'black');
  </script>
</body>
</html>
```



### find



```
$('#box-1').find('.color-2').css('background-color', 'black');
```



`find()`는 선택된 요소의 자녀, 자녀의 자녀, ... 를 골라주되, 조건에 맞는 요소만 골라서 찾아줍니다. 위 코드는 `box-1`의 자녀 요소 중 `color-2` 클래스가 있는 요소의 css를 적용해줍니다.



`children()`은 한 단계 아래의 자녀(직속 자녀)만 찾아주는 반면, `find()`자녀의 자녀의 자녀들까지 그 이하는 모두 찾아낸다는 차이점이 있습니다.



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 box 자체에 `css`가 적용되었고, `box-2`에서는 특정 조건에 맞는 자식 요소에만 `css`가 적용됩니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1').css('background-color', 'black');
    $('#box-2').find('.color-2').css('background-color', 'black');
  </script>
</body>
</html>
```



### siblings



```
$('#btn-1').siblings().text('SELECTED!');
```



`siblings()`는 선택된 요소의 **이웃 요소**들을 골라줍니다. 위 코드에서는 `btn-1`의 모든 이웃 요소에 text를 변경해줍니다. `()` 안에 조건을 넣을 경우, `filter`역할도 함께 해줍니다.



아래 `script` 코드에 유의해서 결과를 살펴보세요. `box-1`에서는 `.color-2` 자기 자신에 `css`가 적용되었고, `box-2`에서는 `.color-2`의 모든 이웃 요소에 `css`가 적용되었습니다. `box-3`에서는 `.color-2`의 모든 이웃 요소에 중 조건에 맞는 요소에만 `css`가 적용됩니다.



- HTML
- CSS

```html
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="box" id="box-1">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-2">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <div class="box" id="box-3">
    <button class="color-1">-</button>
    <button class="color-2">-</button>
    <button class="color-3">-</button>
    <button class="color-4">-</button>
  </div>

  <script
    src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
  <script>
    $('#box-1 .color-2').text('SELECTED!');
    $('#box-2 .color-2').siblings().text('SELECTED!');
    $('#box-3 .color-2').siblings('.color-4').text('SELECTED!');
  </script>
</body>
</html>
```

