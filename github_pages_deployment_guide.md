# AUREN 网站 · GitHub Pages 永久部署指南

## 目标
把 `aurenintimates.com` 指向你的网站，客户输入域名就能访问。

## 整体流程（约20分钟）

```
① 注册 GitHub 账号（5分钟）
② 新建仓库（2分钟）
③ 上传网站文件（3分钟）
④ 开启 GitHub Pages（1分钟）
⑤ 在 Dynadot 设置域名指向（5分钟）
⑥ 等待 DNS 生效（10分钟~2小时）
```

---

## 第一步：注册 GitHub（免费）

1. 打开 `https://github.com`
2. 点 **Sign up**（右上角）
3. 填写：
   - Username：`aurenintimates`（如果被占用，加数字如 `aurenintimates-com`）
   - Email：你的邮箱
   - Password：记住它！
4. 验证邮箱（去邮箱点确认链接）
5. 选 **Free** 套餐 → 完成

---

## 第二步：新建仓库

1. 登录后，点右上角 **+** → **New repository**
2. 填写：
   - Repository name：`aurenintimates.com`（必须一模一样，包括点和com）
   - 描述（可选）：`AUREN official website`
   - 选 **Public**（必须选 Public，Private 需要付费才能用 GitHub Pages）
   - ✅ 勾选 **Add a README file**
3. 点 **Create repository**

---

## 第三步：上传网站文件

在仓库页面：

1. 点 **Add file** → **Upload files**
2. 把以下文件拖进去（从 `website/` 文件夹里找）：
   - `index.html`
   - `images/` 整个文件夹（包含所有产品图）
3. 点底部 **Commit changes**

---

## 第四步：开启 GitHub Pages

1. 在仓库页面，点顶部 **Settings**
2. 左侧菜单找 **Pages**（或搜索 Pages）
3. 在 **Build and deployment** → **Branch** 里：
   - 选 **main**（或 master，看你的默认分支名）
   - 文件夹选 **/ (root)** 
4. 点 **Save**
5. 等1~2分钟，页面会显示：
   > "Your site is live at `https://aurenintimates.github.io/aurenintimates.com`"

---

## 第五步：在 Dynadot 设置域名指向

### 5.1 获取 GitHub Pages 的 IP 地址

在电脑终端（或在线工具）查一下：
```
ping aurenintimates.github.io
```
会得到类似 `185.199.108.153` 的 IP（通常有4个IP，都用）。

### 5.2 登录 Dynadot → 设置 DNS

1. 登录 `dynadot.com`
2. **我的域名** → 点 `aurenintimates.com`
3. 点 **DNS**
4. 删除原有记录（如果有），添加以下 **A 记录**：

| 类型 | 主机名 | 值（IP地址） |
|------|--------|----------------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `aurenintimates.github.io.` |

> ⚠️ CNAME 的值最后有个点 `.`，不要漏掉！

5. 点 **保存**

---

## 第六步：等待 DNS 生效

```
输命令看是否生效：
nslookup aurenintimates.com

生效后会返回上面那4个IP地址。
```

通常需要 **10分钟~2小时**。生效后访问 `https://aurenintimates.com` 就能看到网站了！

---

## 常见问题

### Q：GitHub 仓库名一定要是 `aurenintimates.com` 吗？
A：**推荐是**，这样 GitHub Pages 的默认地址就是 `username.github.io/aurenintimates.com`，和你的域名一致，不容易搞混。

### Q：DNS 生效后网站还是打不开？
A：等更久（最多24小时）。或者用 `https://www.whatsmydns.net` 查全球 DNS 传播进度。

### Q：以后更新网站怎么办？
A：在 GitHub 仓库里，直接编辑 `index.html` 或重新上传图片，保存后自动更新（约1分钟生效）。

---

## 完成后验证

```
✅ 打开 https://aurenintimates.com → 看到 AUREN 网站
✅ 打开 https://www.aurenintimates.com → 自动跳转到上面
✅ 用手机打开 → 布局正常（响应式）
```

---

## 需要帮助？

操作到任何一步卡住了，截图发给我，我实时教你！
