# My Documentation


[Personal](Personal/base.md)  
[Technologies](Technologies/base.md)  
[Technologies](Technologies/Python/base.md) 
[Technologies](Technologies/Django/base.md) 
[Technologies](Technologies/AWS/base.md)  

<script>
      (async () => {
        const response = await fetch('https://api.github.com/repos/shamim1258/Shamim/contents/');
        console.log(response)
        const data = await response.json();
        let htmlString = '<ul>';
        for (let file of data) {
          htmlString += `<li><a href="${file.path}">${file.name}</a></li>`;
        }
        htmlString += '</ul>';
        document.getElementsByTagName('body')[0].innerHTML = htmlString;
      })()
</script>
