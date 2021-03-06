# RPM specfile for the official OVH hubiC client

This client has no UI by itself, just a command line interface.

Run `hubic` after installing to see the commands, or run

```
hubic login <email> <path to local hubiC folder>
```

to start background synchronization.

More information (in french) [on the hubiC forum](https://forums.hubic.com/showthread.php?230-hubic-Linux-sortie-de-la-version-b%EAta).

## RPM repository for Fedora

An RPM repository for Fedora is maintained [in COPR](https://copr.fedorainfracloud.org/coprs/madcat/hubic/).
Run

```
dnf copr enable madcat/hubic
```

to enable it, and

```
dnf install hubic
```

to install the `hubic` package.
