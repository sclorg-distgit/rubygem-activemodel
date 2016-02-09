%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name activemodel


Summary: A toolkit for building modeling frameworks
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.2.5.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/rails.git && cd rails/activemodel && git checkout v4.2.5.1
# tar czvf activemodel-4.2.5.1-tests.tgz test/
Source1: %{gem_name}-4.2.5.1-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix}rubygem(builder) >= 3.1
Requires: %{?scl_prefix}rubygem(builder) < 4.0
# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(activesupport) = %{version}
BuildRequires: %{?scl_prefix}rubygem(bcrypt) => 3.1.2
BuildRequires: %{?scl_prefix}rubygem(builder) => 3.1
BuildRequires: %{?scl_prefix}rubygem(builder) < 4.0
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Rich support for attributes, callbacks, validations, observers,
serialization, internationalization, and testing. It provides a known
set of interfaces for usage in model classes. It also helps building
custom ORMs for use outside of the Rails framework.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}

# load_path is not available, remove its require.
sed -i '1,2d' test/cases/helper.rb

# This depends on Rails, remove for now
rm ./test/cases/railtie_test.rb

# TODO: Run test in order! Otherwise we get a lot of errors.
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:test -e "Dir.glob('./test/**/*_test.rb').sort.each {|t| require t}"
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_docdir}

%changelog
* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 4.2.5.1-1
- Update Rails to 4.2.5.1

* Fri Jan 22 2016 Dominic Cleal <dcleal@redhat.com> 4.2.5-2
- Rebuild for sclo-ror42 SCL

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 4.2.5-1
- Update to activemodel 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 4.2.4-1
- Update to activemodel 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 4.2.3-1
- Update to activemodel 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 4.2.2-1
- Update to activemodel 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-2
- Fix: update tests

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-1
- Update to activemodel 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 4.2.0-1
- Update to activemodel 4.2.0

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to activemodel 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to activemodel 4.1.4
- Stabilize test suite

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 4.1.1-1
- Update to ActiveModel 4.1.1

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Fri Apr 11 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-1
- Update to ActiveModel 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 4.0.3-1
- Update to ActiveModel 4.0.3

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.2-1
- Update to ActiveModel 4.0.2
- Fix changelog

* Mon Nov 11 2013 Josef Stribny <jstribny@redhat.com> - 4.0.1-1
- Update to ActiveModel 4.0.1

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to ActiveModel 4.0.0.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.13-1
- Update to ActiveModel 3.2.13.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-1
- Update to ActiveModel 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.11-1
- Update to ActiveModel 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.10-1
- Update to ActiveModel 3.2.10.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-3
- Fixed the Builder dependencies in .gemspec file.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-2
- Relaxed Builder dependnecy.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-1
- Update to ActiveModel 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.7-1
- Update to ActiveModel 3.2.7.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.6-1
- Update to ActiveModel 3.2.6.
- Remove no longer needed I18n dependency.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.15-1
- Update to ActiveModel 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.13-1
- Update to ActiveModel 3.0.13.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActiveModel 3.0.11.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.10-1
- Update to ActiveModel 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-1
- Update to ActiveModel 3.0.9

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.5-1
- Update to ActiveModel 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.3-3
- Removed unnecessary clean section.

* Mon Jan 31 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.3-2
- Added build dependencies.

* Tue Jan 25 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.3-1
- Upgraded to activemodel 3.0.3
- Added documentation subpackage
- Added test execution during build
- Removed unnecessary cleanup from install section

* Tue Oct 26 2010 Jozef Zigmund <jzigmund@dhcp-29-238.brq.redhat.com> - 3.0.1-1
- Initial package
