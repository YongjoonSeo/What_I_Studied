- 웬만하면 상속되는 속성들 (text관련된 것들이 많다.)

1. `color`

2. `font-family`

3. `font-size`

4. `font-weight`

5. `line-height`

6. `list-style`

7. `text-align`

8. `visibility`

   - 위에 있는 속성들도 항상 상속되는 건 아니다.

     - ex. a태그 -> 속성에 inherit을 사용하여 억지로 상속을 받아오게 할 수 있다.

     ```css
     .div1 {
       color: green;
     }
     
     .div2 {
       color: orange;
     }
     
     .div2 a {
       color: inherit;
     }
     ```

     

