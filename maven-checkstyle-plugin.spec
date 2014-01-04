%{?_javapackages_macros:%_javapackages_macros}
Name:             maven-checkstyle-plugin
Version:          2.10
Release:          2.0%{?dist}
Summary:          Plugin that generates a report regarding the code style used by the developers

License:          ASL 2.0
URL:              http://maven.apache.org/plugins/%{name}

Source0:          http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:           %{name}-maven-core-dep.patch

BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-plugin-plugin >= 2.5.1
BuildRequires:    plexus-containers-component-metadata >= 1.5.1
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-compiler-plugin >= 2.0.2
BuildRequires:    maven-jar-plugin >= 2.2
BuildRequires:    maven-install-plugin >= 2.2
BuildRequires:    checkstyle >= 5.6
BuildRequires:    plexus-cli >= 1.2
BuildRequires:    maven-artifact-manager 
BuildRequires:    plexus-resources
BuildRequires:    maven-doxia-sitetools
BuildRequires:    maven-doxia-sink-api

Requires:         maven
Requires:         maven-shared-reporting-impl >= 2.0.4.3
Requires:         maven-doxia-sink-api
Requires:         maven-doxia-sitetools >= 1.0
Requires:         maven-doxia-tools >= 1.0.2
Requires:         plexus-containers-container-default
Requires:         plexus-resources
Requires:         plexus-utils >= 1.5.6
Requires:         plexus-velocity >= 1.1.7
Requires:         checkstyle >= 5.6
Requires:         velocity >= 1.5
Requires:         apache-commons-collections >= 3.2.1
Requires:         junit >= 3.8.2
Requires:         maven-plugin-testing-harness >= 1.2

Requires:         java >= 1:1.6.0
Requires:         jpackage-utils

Provides:         maven2-plugin-checkstyle = %{version}-%{release}
Obsoletes:        maven2-plugin-checkstyle <= 0:2.0.8

%description
Generates a report on violations of code style and optionally fails the build
if violations are detected.

%package javadoc

Summary:          Javadoc for %{name}
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 

%build
# During testing, component descriptors can't be found. 
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.failure.ignore

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Mat Booth <fedora@matbooth.co.uk> - 2.10-1
- Update to 2.10, require checkstyle 5.6, rhbz #915219

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.9.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 02 2013 Michal Srb <msrb@redhat.com> - 2.9.1-4
- Migrated from maven-doxia to doxia subpackages (Resolves: #889144)

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-3
- Install NOTICE files
- Resolves: rhbz#880265

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 5 2012 Alexander Kurtakov <akurtako@redhat.com> 2.9.1-1
- Update to 2.9.1.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 2 2011 Alexander Kurtakov <akurtako@redhat.com> 2.8-1
- Update to 2.8.

* Thu Sep 15 2011 Tomas Radej <tradej@redhat.com> - 2.7-1
- Updated to 2.7
- Guideline fixes

* Thu Jun 9 2011 Alexander Kurtakov <akurtako@redhat.com> 2.6-5
- Fix checkstyle groupId.

* Thu Jun 9 2011 Alexander Kurtakov <akurtako@redhat.com> 2.6-4
- Build with maven 3.x.
- Guideline fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 5 2010 Chris Spike <chris.spike@arcor.de> 2.6-2
- Changed BR from 'commons-collections' to 'apache-commons-collections'

* Sat Oct 2 2010 Chris Spike <chris.spike@arcor.de> 2.6-1
- Updated to latest upstream version

* Mon Jul 19 2010 Chris Spike <chris.spike@arcor.de> 2.5-3
- Eventually really fixed Requires for plexus-containers-container-default and 
  plexus-resources (#616202)

* Mon Jul 19 2010 Chris Spike <chris.spike@arcor.de> 2.5-2
- Removed BuildArch from javadoc subpackage
- Fixed Requires for plexus-containers-container-default and 
  plexus-resources (#616202)

* Thu Jul 15 2010 Chris Spike <chris.spike@arcor.de> 2.5-1
- Initial version of the package
