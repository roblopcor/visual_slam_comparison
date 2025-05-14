#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "obindex2::obindex2" for configuration "Release"
set_property(TARGET obindex2::obindex2 APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(obindex2::obindex2 PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libobindex2.so"
  IMPORTED_SONAME_RELEASE "libobindex2.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS obindex2::obindex2 )
list(APPEND _IMPORT_CHECK_FILES_FOR_obindex2::obindex2 "${_IMPORT_PREFIX}/lib/libobindex2.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
