# PythonOnline
<font face=����>
### 1 д��ǰ��
</font><font face=���� size=3>
���õ���������������ҵĸ�����վ��<a href="liushangyu.xyz" target=new>Atlantis</a>

�����Ŀ�ṩ��һ����python��������������еĹ��ߣ�����ֻ��Ҫ��������д���Լ��Ĵ��룬���`�ύ����`���ɽ��������͵�server��̨����̨���г���󽫱�׼����ͱ�׼���󷵻���ǰ�ˣ���ҳ���·����õ���������н�������������յĽ���Ч����

<div align=center><img src="liushangyu.xyz/uploads/kindeditor/2019/2/28363a02-38ab-11e9-b85f-00163e0c3e76.gif" width=100% /></div>

�����ʵ���Ŀ��ԭ����Ϊ����һ����������������ģ�����չʾ��ϣ����ģ�������ڷ�������̨��ͨ����ҳ�ύ���������ݴ��͸�ģ�ͣ���ǰ���ٽ�ģ�͵����չʾ����������ģ�ͻ�û��ѵ���������Ҿʹ�������PythonOnline��������Ŀ���в��ԡ�

����һ���޿�ܵ�webʵ�飬ֻ��Ҫһ�����ؿ��õ�python3���л�����һ���ȸ���������ɡ����ǽ�ʹ��python��Ϊsever��̨�������ԣ�ʹ��jQuery��ǰ�˱��ύ��ʹ��bootstrap��Ϊǰ��UI�⡣
</font><font face=����>
### 2 ��дHTTP������
</font><font face=���� size=3>
ʵ��HTTP�������Ĵ�����Ҫ�ο��˲���<a href="https://www.cnblogs.com/xinyangsdut/p/9099623.html" target=new>Pythonʵ�ּ�HTTP������</a>��`���ض�̬����(����wsgi��`һ�ڸ��������̴��룬�������̵Ļ����������Ķ��������ڱ��м�����һ�������`CMD`�Դ��ݳ���ԭ�ġ�������ʹ�õ���`post`���������Բ��������Ǽ�������ͷ�ĺ���ġ�����Ҫע�⣬ԭ�����õ���`get`������������������ͷ֮�еģ���һ��һ��Ҫע�⡣���������ӵĴ������Ļ�ȡ�����ֵ�Ĵ��룺
```python
...
request_datas_line = unquote(request_lines[-1].decode("utf-8").replace("+", " "))
...
params = {}
if request_datas_line:
    for param in request_datas_line.split('&'):
        if '=' in param:
            tmp = re.match(r"([^=]+)=(.*)", param, re.DOTALL)
            params[tmp.group(1).upper()] = tmp.group(2)
...
```
ע�������`urllib.parse.unquote`��������������URL�ġ��ڴ��ݲ������ݵ�ʱ��ǰ�˻Ὣ���ݽ���URL���룬���ո��滻Ϊ�Ӻţ����Ӻš��Ǻš����ŵȷ��Ž����滻��������URL�е�ת���ַ���ͻ����������Ҫ�õ�����ԭ����Ҫ����URL���룬�����Ӻ��滻Ϊ�ո�

�������֮���Ƿ�����������ӻ��д�ʵ�飬Ŀǰֻ֪��`get`����ʱ�ĸ�ʽ��ˡ�

������`application()`��params�ֵ��޸ĳ����£���ԭ���ֵ��м���ղŻ�õĲ������ݡ�
```python
params.update(dict({ "PATH_INFO": file_name, "METHOD": method}))
```
���ǿ��Կ������溯���Ĺ��ܼ��ǵ���URL��ָ�����ļ�m��application����������ȡ�䷵��ֵ��Ϊ��Ӧ���ݣ�
```python
response_body = m.application(params, self.start_response)
```
��ô�������Ĺ������Ǳ�д��Ӧ�ű���
</font><font face=����>
### 2 ��д��̨��Ӧ�ű�
</font><font face=���� size=3>
����server.py��ͬ��Ŀ¼���½��ļ���wsgi����wsgi�ļ������½��ļ�run.py��Ϊ��Ӧ�ű����ⲿ��Ҳ���Բο��Ͻ��ᵽ�Ĳ��ͣ���`application()`�����м������´��룺
```python
if "CMD" in params and params["CMD"].strip():
	with open("tmp.py", 'w') as writer:
		writer.write(params["CMD"])
	data = os.popen("python tmp.py 2>err.log", 'r').read()
	if not data:
		data = open("err.log", 'r', encoding="utf-8").read()
	result = ""
	for line in data.split('\n'):
		result += "<p>{}</p>".format(line)
	return result
else:
	return "Bad Parameters!"
```
�������������ֵ�����`CMD`�������Ҳ�����ֵ��Ϊ�գ���ô���½�һ��`tmp.py`����ʱpython�ļ�����`CMD`�Ĳ���ֵ����ǰ������Ĵ���д����ʱ�ļ��У�Ȼ��ʹ��`os.popen()`�������иó���ע�������`os.popen()`����ֻ�ܲ�׽��׼��������������ڳ������н�����������еĳ������쳣������ʹ��`try`�����������׽�����κ���Ϣ��ͬʱdataҲֻ�ܵõ��ա����������������м���`2>err.log`���������Ϣ���ļ�`err.log`����Ҫע�⣬��������ض���������в����пո񡣼��dataΪ��ʱ����������־����Ϣ������ǰ�ˡ�Ϊ����ǰ���ܹ�������ʾ��������Ҫ�����ÿһ�л���`<p></p>`��ǩ�����Ķ��䡣

���ǰ�˴����Ĳ�����ֵ�д�����ô����`Bad Parameters!`��ʾ��Ϣ���������ԡ�

����������Ҫ��дһ����������۵�ǰ�˽��棬��ʵ�ֱ����ύ��
</font><font face=����>
### 3 ��дǰ�˽���
</font><font face=���� size=3>
�������ȱ�дһ����ª��HTML�����ܣ��������������������ύ��ť�������õ���bootstrapǰ��UI�⣬��Ҫ��header�а�������ļ������ӣ�
```htmlbars
<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
```
����ֻ��Ϊ�˽��ⷽ���һ�ν�ѡ���������ʽ���HTMLȫ�Ļ����Ʋ�GitHub��
```htmlbars
<div class="card">
    <div class="card-body">
        <div id="pay-invoice">
            <div class="card-body">
                <div class="card-title">
                    <h3 class="text-center">Python Online</h3>
                </div>
                <hr>
                <form id="form" action="/run.py" novalidate="novalidate">
                    <div class="form-group">
                        <label class="control-label mb-1">������Դ����</label>
                        <textarea type="text" id="cmd" class="form-control" spellcheck="false"></textarea>
                    </div>
                    <div>
						<button class="btn btn-lg bt-run" id="run">�ύ����</button>
						<button class="btn btn-lg bt-reset" id="reset">���ô���</button>
						<button class="btn btn-lg bt-clear" id="clear">�������</button>
                    </div>
                </form>
                <div style="margin-top: 60px;">
                    <label class="control-label mb-1">�������н��</label>
					<div class="result" id="result"></div>
				</div>
			</div>
        </div>
    </div>
</div>
```
���ڱ����ύ���ܣ����ǿ���ֱ��ʹ��`javascript`�Դ���`form.submit()`�����ύ������û����ȡ�ύ�󷵻ص����ݡ�������ʹ����`jQuery`��`ajaxSubmit()`������
```javascript
$("#run").on('click', function() {
	$("#form").ajaxSubmit({
		type: 'post',
		data: {
			'cmd': $('#cmd').val()
		},
		dataType:'text',
		contentType: "application/x-www-form-urlencoded; charset=UTF-8",
		success: function(msg) {
			var time = "<p>[" + new Date().toLocaleTimeString() + "]</p>";
			$("#result").append(time + msg);
			var scrollHeight = $('#result').prop("scrollHeight");
  			$('#result').animate({scrollTop: scrollHeight}, 400);
		}
	});
	return false;
});
```
Ϊ�˸��õ��û����飬��ʹÿ����������������������ǰ��������棬���ҹ������Զ��������ײ�����ʾ���½�������⻹�ڽ����ͷ��������ʱ����Ϣ�������ֲ�ͬ�Ĵ������н�����ڵ���ǰ�˵Ĺ������������˼�����Ҫ�����⣺

**������������** HTML�е������ַ������������ʾΪ���룬ֻ��Ҫ��header�м��룺
```htmlbars
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
```

**�ظ��ύ����** ����ʹ��ajaxSubmit�ύ�����ֵľ������⡣һ����˵����������ԭ��

+ ��`<form>`��ǩ��������`Action`������`ajaxSubmit()`����������`URL`  
+ ��`ajaxSubmit()`���ְ�����һ��`on('submit')`��`submit()`  

**Textarea��ʹ��TAB** ��ҳ���е�TAB��Ĭ����������ת����ģ����Ǽ������´��벶׽Textarea�е�TAB���룬������ת��Ϊ�ĸ��ո�
```javascript
$("textarea").on('keydown', function(e) {
    if (e.keyCode == 9) {
        e.preventDefault();
        var indent = '    ';
        var start = this.selectionStart;
        var end = this.selectionEnd;
        var selected = window.getSelection().toString();
        selected = indent + selected.replace(/\n/g, '\n' + indent);
        this.value = this.value.substring(0, start) + selected
                + this.value.substring(end);
        this.setSelectionRange(start + indent.length, start
                + selected.length);
    }
})
```
�����һ���д��������մ�����������������İ�ť���ܣ������ﲻ������������������������`localhost:8000`���ɿ����������ĸ����Ľ���Ч���ˡ�
</font><font face=����>
### 4 δ������
</font><font face=���� size=3>
���ǿ��Ը���վ����һЩСӦ�á��ҽ��������м���һ��APPS���棬����һЩ����˼��С���ߡ�����֮ǰд���Ķ�ά�����ɡ��ַ���ת��������ɫ��ȡ���������˹����ܵȵȡ����������ͻ��ʹ�úܶิ�ӵ�Python�����ܹ���ǰ̨�����ã�Ϊδ�����������޿��ܣ���ָ�����ҵ���Ŀ��δ������
</font>