---
layout: post
title:
category : Oracle
tags : [Oracle, DBA]
---

##Tomcat HTTPS with JSSE

To create a new keystore from scratch, containing a single self-signed Certificate, execute the following from a terminal command line:

	[root@server ssl]# keytool -genkey -alias tomcat -keyalg RSA -keystore tomcat.keystore
	Enter keystore password:  
	Re-enter new password: 
	What is your first and last name?
	  [Unknown]:  dylan
	What is the name of your organizational unit?
	  [Unknown]:  itsection
	What is the name of your organization?
	  [Unknown]:  itcompany
	What is the name of your City or Locality?
	  [Unknown]:  sz
	What is the name of your State or Province?
	  [Unknown]:  gd
	What is the two-letter country code for this unit?
	  [Unknown]:  cn
	Is CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn correct?
	  [no]:  y
	
	Enter key password for <tomcat>
		(RETURN if same as keystore password):  
	Re-enter new password: 


Finally, you will be prompted for the key password, which is the password specifically for this Certificate (as opposed to any other Certificates stored in the same keystore file). You MUST use the same password here as was used for the keystore password itself. This is a restriction of the Tomcat implementation. (Currently, the keytool prompt will tell you that pressing the ENTER key does this for you automatically.)

导出证书：

	[test@server tomcat]$ keytool -export -alias tomcat -keystore tomcat.keystore -file tomcat.cer -storepass 000000
	Certificate stored in file <tomcat.cer>

导入证书：

	[test@server tomcat]$ keytool -import -file tomcat.cer -storepass 000000 -keystore tomcat.truststore -alias tomcat
	Owner: CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn
	Issuer: CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn
	Serial number: 512c076d
	Valid from: Tue Feb 26 08:53:01 CST 2013 until: Mon May 27 08:53:01 CST 2013
	Certificate fingerprints:
		 MD5:  E9:7C:24:E2:26:C0:6A:61:CA:CE:92:E7:B8:90:88:4A
		 SHA1: E7:07:34:33:97:58:65:FD:E0:85:51:F3:C9:FB:A7:CA:DA:3E:FD:56
		 Signature algorithm name: SHA1withRSA
		 Version: 3
	Trust this certificate? [no]:  y
	Certificate was added to keystore


导入证书到JRE信任证书中：

	[test@server tomcat]$ keytool -import -alias tomcat -keystore /usr/java/jdk1.6.0_33/jre/lib/security/cacerts -trustcacerts -file tomcat.cer -storepass 000000
	Owner: CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn
	Issuer: CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn
	Serial number: 512c076d
	Valid from: Tue Feb 26 08:53:01 CST 2013 until: Mon May 27 08:53:01 CST 2013
	Certificate fingerprints:
		 MD5:  E9:7C:24:E2:26:C0:6A:61:CA:CE:92:E7:B8:90:88:4A
		 SHA1: E7:07:34:33:97:58:65:FD:E0:85:51:F3:C9:FB:A7:CA:DA:3E:FD:56
		 Signature algorithm name: SHA1withRSA
		 Version: 3
	Trust this certificate? [no]:  y
	Certificate was added to keystore
	keytool error: java.io.FileNotFoundException: /usr/java/jdk1.6.0_33/jre/lib/security/cacerts (Permission denied)

删除已经存在的$JAVA_HOME/jre/lib/security/cacerts：

	[root@server tomcat]# rm /usr/java/jdk1.6.0_33/jre/lib/security/cacerts 
	rm: remove regular file `/usr/java/jdk1.6.0_33/jre/lib/security/cacerts'? y

重新导入：

	[root@server tomcat]# keytool -import -alias tomcat -keystore /usr/java/jdk1.6.0_33/jre/lib/security/cacerts -trustcacerts -file tomcat.cer -storepass 000000
	Owner: CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn
	Issuer: CN=dylan, OU=itsection, O=itcompany, L=sz, ST=gd, C=cn
	Serial number: 512c076d
	Valid from: Tue Feb 26 08:53:01 CST 2013 until: Mon May 27 08:53:01 CST 2013
	Certificate fingerprints:
		 MD5:  E9:7C:24:E2:26:C0:6A:61:CA:CE:92:E7:B8:90:88:4A
		 SHA1: E7:07:34:33:97:58:65:FD:E0:85:51:F3:C9:FB:A7:CA:DA:3E:FD:56
		 Signature algorithm name: SHA1withRSA
		 Version: 3
	Trust this certificate? [no]:  y
	Certificate was added to keystore


server.xml配置：

	<!-- Define a SSL HTTP/1.1 Connector on port 8443
    	This connector uses the JSSE configuration, when using APR, the 
     	connector should be using the OpenSSL style configuration
        described in the APR documentation -->
    <Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"
               maxThreads="150" scheme="https" secure="true"
			   keystoreFile="tomcat.keystore" keystorePass="000000"
               clientAuth="false" sslProtocol="TLS" />

##errors

###when private key password and keystore password differ

When your private key password and keystore password should be the same. If they differ, you will get an error along the lines of java.io.IOException:Cannot recover key as following:
	
	INFO: Initializing Coyote HTTP/1.1 on http-8080
	Feb 26, 2013 9:06:53 AM org.apache.coyote.http11.Http11Protocol init
	SEVERE: Error initializing endpoint
	java.io.IOException: Cannot recover key
	        at org.apache.tomcat.util.net.jsse.JSSESocketFactory.init(JSSESocketFactory.java:465)
	        at org.apache.tomcat.util.net.jsse.JSSESocketFactory.createSocket(JSSESocketFactory.java:130)
	        at org.apache.tomcat.util.net.JIoEndpoint.init(JIoEndpoint.java:538)
	        at org.apache.coyote.http11.Http11Protocol.init(Http11Protocol.java:176)
	        at org.apache.catalina.connector.Connector.initialize(Connector.java:1014)
	        at org.apache.catalina.core.StandardService.initialize(StandardService.java:680)
	        at org.apache.catalina.core.StandardServer.initialize(StandardServer.java:795)
	        at org.apache.catalina.startup.Catalina.load(Catalina.java:524)
	        at org.apache.catalina.startup.Catalina.load(Catalina.java:548)
	        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	        at java.lang.reflect.Method.invoke(Method.java:616)
	        at org.apache.catalina.startup.Bootstrap.load(Bootstrap.java:261)
	        at org.apache.catalina.startup.Bootstrap.main(Bootstrap.java:413)
	Feb 26, 2013 9:06:53 AM org.apache.catalina.startup.Catalina load
	SEVERE: Catalina.start
	LifecycleException:  Protocol handler initialization failed: java.io.IOException: Cannot recover key
	        at org.apache.catalina.connector.Connector.initialize(Connector.java:1016)
	        at org.apache.catalina.core.StandardService.initialize(StandardService.java:680)
	        at org.apache.catalina.core.StandardServer.initialize(StandardServer.java:795)
	        at org.apache.catalina.startup.Catalina.load(Catalina.java:524)
	        at org.apache.catalina.startup.Catalina.load(Catalina.java:548)
	        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)

Note: your private key password and keystore password should be the same. If they differ, you will get an error along the lines of java.io.IOException: Cannot recover key, as documented in [Bugzilla issue 38217](https://issues.apache.org/bugzilla/show_bug.cgi?id=38217), which contains further references for this issue.

使用keytool更改private key密码，使与keystore的密码一致，则可以正常访问：

	keytool -keypasswd -alias tomcat -keypass 123456 -new 000000 -keystore tomcat.keystore -storepass 000000

