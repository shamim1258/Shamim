# Python Preperation Questions

Text[Python](Shamim/Technology/Python/base.md)
Text[Python2](../../Technology/Python/base.md)

{% site.github.public_repositories %}
{% site.github.Shamim %}
{% site.github.shamim1258 %}

{% for repo in site.github.public_repositories %}
[{{ repo.Shamim }}]({{ repo.html_url }})
: {{ repo.description }}
{% endfor %}


1. How is memory managed in Python? 
<details><summary>Text[Python]((../../Technology/Python/base.md)
  Text[Python2](/../../Technology/Python/base.md)
  <a href="https://shamim1258.github.io/Shamim/Technology/Python/base.md">Python Details Link Href</a>
  </summary>
  Text[Python]((../../Technology/Python/base.md)
  Text[Python2](/../../Technology/Python/base.md)
Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated to Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.
</details>