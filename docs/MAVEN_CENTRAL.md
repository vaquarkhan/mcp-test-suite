# Publish to Maven Central (guide)

Artifact: **`io.github.vaquarkhan:mcp-test-suite-junit5`**  
Same `groupId` style as your other `io.github.vaquarkhan` Central packages.

Today the JAR is only on **GitHub Packages** / Releases. After you add the secrets below, CI can publish to **Maven Central** (searchable on Central / mvnrepository).

---

## What you need (checklist)

| Item | Where | Notes |
|------|--------|------|
| 1. Central Portal account | https://central.sonatype.com/ | Sign in with the same account that owns `io.github.vaquarkhan` |
| 2. Namespace verified | Portal → Namespaces | `io.github.vaquarkhan` must already be verified (you said AIV is on Central — reuse that) |
| 3. User token | Portal → **Account** → **Generate User Token** | Creates **username** + **password** (not your login password) |
| 4. GPG key | Local machine | Used to sign JARs / POM / sources / javadoc |

---

## Step 1 — Confirm namespace

1. Open https://central.sonatype.com/
2. **Namespaces** → confirm **`io.github.vaquarkhan`** is verified.
3. If you only have another namespace, either:
   - publish under that `groupId`, or  
   - verify `io.github.vaquarkhan` (GitHub proof flow in the Portal).

Our POM already uses:

```xml
<groupId>io.github.vaquarkhan</groupId>
<artifactId>mcp-test-suite-junit5</artifactId>
<version>4.0.0</version>
```

---

## Step 2 — Create a Central user token

1. https://central.sonatype.com/account  
2. **Generate User Token**  
3. Save both values:

| Secret name (GitHub) | Value |
|----------------------|--------|
| `CENTRAL_USERNAME` | token **username** from Portal |
| `CENTRAL_PASSWORD` | token **password** from Portal |

---

## Step 3 — GPG key (signing)

### Create (or reuse) a key

```bash
# list existing keys
gpg --list-secret-keys --keyid-format LONG

# if you need a new one:
gpg --full-generate-key
# RSA 4096, expire 2y+, name/email matching your Central profile is fine
```

Note the **KEY ID** (last 16 hex chars), e.g. `3AA5C34371567BD2`.

### Export for GitHub Actions

```bash
# private key (ASCII armored) — paste entire output into a secret
gpg --armor --export-secret-keys YOUR_KEY_ID

# passphrase you set when creating the key
```

| Secret name (GitHub) | Value |
|----------------------|--------|
| `GPG_PRIVATE_KEY` | Full armored block (`-----BEGIN PGP PRIVATE KEY BLOCK-----` …) |
| `GPG_PASSPHRASE` | Passphrase for that key |
| `GPG_KEY_ID` | Optional but useful; KEY ID used by `maven-gpg-plugin` |

### Publish public key (required by Central)

```bash
gpg --keyserver keyserver.ubuntu.com --send-keys YOUR_KEY_ID
# or
gpg --keyserver keys.openpgp.org --send-keys YOUR_KEY_ID
```

Wait until the key is fetchable before the first publish.

---

## Step 4 — Add secrets to this GitHub repo

Repo: **vaquarkhan/mcp-test-suite**

1. GitHub → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
2. Create all of:

```text
CENTRAL_USERNAME
CENTRAL_PASSWORD
GPG_PRIVATE_KEY
GPG_PASSPHRASE
```

Optional: `GPG_KEY_ID`

Use the **same** Central token / GPG key you use for AIV if that namespace and signing identity are already trusted.

---

## Step 5 — Publish from Actions

Workflow: **Publish language adapters** (updated to support Central).

1. **Actions** → **Publish language adapters** → **Run workflow**
2. Set:
   - `version`: `4.0.0` (or next version if `4.0.0` was already claimed on Central)
   - `dry_run`: `false`
   - `maven_central`: `true`
3. Wait for the **junit5-central** job.

When green, search:

- https://central.sonatype.com/artifact/io.github.vaquarkhan/mcp-test-suite-junit5  
- https://repo1.maven.org/maven2/io/github/vaquarkhan/mcp-test-suite-junit5/

Propagation can take **minutes to a few hours**.

---

## Step 6 — Install after Central is live (no GitHub PAT)

**Maven**

```xml
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

**Gradle**

```kotlin
dependencies {
  testImplementation("io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0")
}
```

No `settings.xml` GitHub server required.

---

## Local dry-run (optional)

With secrets in `~/.m2/settings.xml`:

```xml
<servers>
  <server>
    <id>central</id>
    <username>${env.CENTRAL_USERNAME}</username>
    <password>${env.CENTRAL_PASSWORD}</password>
  </server>
</servers>
```

```bash
cd adapters/junit5
export CENTRAL_USERNAME=...
export CENTRAL_PASSWORD=...
# import GPG key and set passphrase env for maven-gpg-plugin
mvn -B -Pmaven-central clean deploy -DskipTests
```

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `401` / unauthorized to Central | Wrong token; regenerate User Token; server id must be `central` |
| GPG sign failed | Bad `GPG_PRIVATE_KEY` / passphrase; key not imported in the job |
| Validation failed (POM) | Ensure `name`, `description`, `url`, `licenses`, `developers`, `scm` present (already in our POM) |
| Namespace not allowed | Verify `io.github.vaquarkhan` in Central Portal |
| Version already exists | Bump version (Central versions are immutable) |

---

## Related

- POM profile: `adapters/junit5/pom.xml` → profile `maven-central`
- Workflow: `.github/workflows/publish-adapters.yml` → job `junit5-central`
- GitHub Packages (interim): [packages/3158511](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)
