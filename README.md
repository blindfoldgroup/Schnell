# Schnell

## on Linux

### Add 'Open in Schnell'

```
wget -qO- https://raw.githubusercontent.com/blindfoldgroup/Schnell/master/install.sh | bash
```

### Remove 'Open in Schnell'

```
rm -f ~/.local/share/nautilus-python/extensions/schnell-nautilus.py

```

## on Mac
### create an application using the following apple script in Automator. Save it as 'OpenInSchnell' or anything other name you like. Then go to Applications/ directory in finder and drag to newly created app holding command button on finder toolbar

```
tell application "Finder"
	set theWindow to window 1
	set thePath to (POSIX path of (target of theWindow as alias))
	set theCommand to "/usr/bin/open -n -b \"com.blindfold.schnell\" --args " & thePath
	do shell script (theCommand)
end tell
```

## on Windows

schnell automatically adds `Open Schnell here` (Admin Mode as well) after installation.
