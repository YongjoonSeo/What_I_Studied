제이쿼리를 사용하면 애니메이션도 보다 쉽게 만들 수 있습니다.



### CSS 적용하기



```
$("div").animate({left: '250px'});
```



와 같이 작성하면 `div`태그가 `left: 250px`만큼 이동합니다.



- HTML
- CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery Animation</title>
  <meta charset="utf-8" />
  <link href="css/styles.css" rel="stylesheet" />
</head>
<body>

<button>Start Animation</button>

<div></div>

<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>

<script> 
$(document).ready(function() {
  $("button").on('click', function() {
    $("div").animate({left: '250px'});
  });
});
</script> 

</body>
</html>
```



### 여러 CSS 동시에 적용하기



```
$("div").animate({left: '250px', opacity: '0.5'});
```



와 같이 작성하면 `div`태그가 `left: 250px`만큼 이동하면서 동시에 `opacity: 0.5`가 적용됩니다.



- HTML
- CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery Animation</title>
  <meta charset="utf-8" />
  <link href="css/styles.css" rel="stylesheet" />
</head>
<body>

<button>Start Animation</button>

<div></div>

<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>

<script> 
$(document).ready(function() {
  $("button").on('click', function() {
    $("div").animate({left: '250px', opacity: '0.5'});
  });
});
</script> 

</body>
</html>
```



### 여러 CSS 순서대로 적용하기



```
$("div").animate({left: '250px', opacity: '0.5'});
```



와 달리,



```
$("div").animate({left: '250px'});
$("div").animate({opacity: '0.5'});
```



라고 작성하면 `div`태그가 `left: 250px`만큼 이동한 후, `opacity: 0.5`가 적용됩니다.



- HTML
- CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery Animation</title>
  <meta charset="utf-8" />
  <link href="css/styles.css" rel="stylesheet" />
</head>
<body>

<button>Start Animation</button>

<div></div>

<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>

<script> 
$(document).ready(function() {
  $("button").on('click', function() {
    $("div").animate({left: '250px'});
    $("div").animate({opacity: '0.5'});
  });
});
</script> 

</body>
</html>
```



### CSS 반복 적용하기



```
$("div").animate({left: '+=250px'});
```



와 같이 작성하면 `div`태그가 `left: 250px`만큼, 버튼을 누를 때 마다 계속해서 이동합니다.



- HTML
- CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery Animation</title>
  <meta charset="utf-8" />
  <link href="css/styles.css" rel="stylesheet" />
</head>
<body>

<button>Start Animation</button>

<div></div>

<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>

<script> 
$(document).ready(function() {
  $("button").on('click', function() {
    $("div").animate({left: '+=250px'});
  });
});
</script> 

</body>
</html>
```



### CSS 적용 속도 조절하기



```
$("div").animate({left: '250px'}, 1000);
```



와 같이 작성하면 `div`태그가 `left: 250px`만큼 1000ms, 즉 1초 동안 이동합니다. 이 값으로는 숫자 뿐 아니라, `slow`, `fast`로도 사용이 가능합니다.



- HTML
- CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery Animation</title>
  <meta charset="utf-8" />
  <link href="css/styles.css" rel="stylesheet" />
</head>
<body>

<button>Start Animation</button>

<div></div>

<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>

<script> 
$(document).ready(function() {
  $("button").on('click', function() {
    $("div").animate({left: '250px'}, 1000);
  });
});
</script> 

</body>
</html>
```



### 애니메이션 이펙트 적용하기



```
$("div").animate({left: '250px'}, 1000, 'easeOutElastic');
```



와 같이 작성하면 `div`태그가 `left: 250px`만큼 1초 동안 이동하되, `easeOutElastic` 효과가 적용됩니다.



이런 애니메이션 이펙트를 'Easing'이라고 부르는데, 'Easing' 효과에는 `linear`, `swing`, `easeInBounce`, `easeOutBounce`, `easeInOutBounce` 등 다양한 종류가 있습니다.



다양한 종류의 Easing은 [여기](https://easings.net/)에서 확인할 수 있습니다.



'Easing'을 사용하기 위해서는 jQueryUI 코드도 추가해주어야 합니다.



```js
<script
  src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"
  integrity="sha256-T0Vest3yCU7pafRw9r+settMBX6JkKN06dqBnpQ8d30="
  crossorigin="anonymous"></script>
```



jQuery UI CDN은 [여기](https://code.jquery.com/ui/)에서 가져올 수 있습니다.



- HTML
- CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>jQuery Animation</title>
  <meta charset="utf-8" />
  <link href="css/styles.css" rel="stylesheet" />
</head>
<body>

<button>Start Animation</button>

<div></div>

<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>
<script
  src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"
  integrity="sha256-T0Vest3yCU7pafRw9r+settMBX6JkKN06dqBnpQ8d30="
  crossorigin="anonymous"></script>
<script> 
$(document).ready(function() {
  $("button").on('click', function() {
    $("div").animate({left: '250px'}, 1000, 'easeOutElastic');
  });
});
</script> 

</body>
</html>
```

