Name:             maven-checkstyle-plugin
Version:          2.6
Release:          5
Summary:          Plugin that generates a report regarding the code style used by the developers
Group:            Development/Java
License:          ASL 2.0
URL:              http://maven.apache.org/plugins/%{name}

Source0:          http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:        noarch

BuildRequires:    java-devel >= 0:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    maven2 >= 2.2.1
BuildRequires:    maven-plugin-plugin >= 2.5.1
BuildRequires:    plexus-containers-component-metadata >= 1.5.1
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-compiler-plugin >= 2.0.2
BuildRequires:    maven-surefire-maven-plugin
BuildRequires:    maven-jar-plugin >= 2.2
BuildRequires:    maven-install-plugin >= 2.2
BuildRequires:    checkstyle >= 5.0
BuildRequires:    plexus-cli >= 1.2

Requires:         maven2 >= 2.2.1
Requires:         maven-shared-reporting-impl >= 2.0.4.3
Requires:         maven-doxia >= 1.0
Requires:         maven-doxia-sitetools >= 1.0
Requires:         maven-doxia-tools >= 1.0.2
Requires:         plexus-containers-container-default
Requires:         plexus-resources
Requires:         plexus-utils >= 1.5.6
Requires:         plexus-velocity >= 1.1.7
Requires:         checkstyle >= 5.0
Requires:         velocity >= 1.5
Requires:         apache-commons-collections >= 3.2.1
Requires:         junit >= 3.8.2
Requires:         maven-plugin-testing-harness >= 1.2

Requires:         java >= 0:1.6.0
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

Provides:         maven2-plugin-checkstyle = %{version}-%{release}
Obsoletes:        maven2-plugin-checkstyle <= 0:2.0.8

%description
Generates a report on violations of code style and optionally fails the build
if violations are detected.

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%doc LICENSE
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

