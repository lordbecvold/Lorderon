<?php
	include 'config/site.php';
	include 'config/db.php';
?>
<!doctype html>
<html>
<head>
		<meta charset="ANSI" />
		<title><?php print $name; ?></title>
		<meta name="author" content="Lordbecvold">
		<meta name="viewport" content="width=device-width, initial-scale=1,  maximum-scale=1, user-scalable=no">
		<link rel="shortcut icon" href="img/favicon.png" type="image/png" />
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="css/style.css" />
		<link rel="stylesheet" type="text/css" href="css/font-awesome.min.css" />
		<link rel="stylesheet" type="text/css" href="css/perfect-scrollbar.css" />
		<link rel="stylesheet" type="text/css" href="css/jquery.fullpage.css" />
		<link rel="stylesheet" type="text/css" href="css/lightbox.min.css" />	
		<script src="js/jquery.min.js"></script>
		<script src="js/jquery.slimscroll.js"></script>
		<script src="js/perfect-scrollbar.jquery.js"></script>
		<script src="js/perfect-scrollbar.js"></script>
		<script src="js/jquery.fullpage.js"></script>
		<script src="js/main.js"></script>
	</head>
	<body>
		<nav id="mainnav">
			<ul>
				<li><a class="first" href="#intro">Úvod</a></li>
				<li><a href="#registration">Registrace</a></li>
				<li><a href="#download">Stažení</a></li>
				<li><a href="#ranking">žebříček hráčů</a></li>
				<li><a href="#vop">Pravidla</a></li>
				<li><a href="#problems">Řešení problémů</a></li>
				<li><a href="https://discord.gg/eGKhwGW">Discord</a></li>
				<li><a href="/presentation/index.html">Prezentace</a></li>
			</ul>
		</nav>
		<nav id="footnav">
			<ul>
				<li><a class="first" target="_blank" href="http://lorderon.eu/">Provided by Lukáš Bečvář</a></li>
			</ul>
		</nav>
		<div id="social">
			<?php
				if($facebook_page)
					print "<a href='$facebook_page' class='scircle'><span class='fa fa-facebook'></span></a>";
				if($youtube_canal)
					print "<a href='$youtube_canal' class='scircle'><span class='fa fa-youtube-play'></span></a>";
				if($twitter_page)
					print "<a href='$twitter_page' class='scircle'><span class='fa fa-twitter'></span></a>";
			?>
		</div>
		<div id="getContent"></div>
		<div id="houses"></div>
		<div id="border"></div>
		<?php if($online_players) {
				print '<div id="sec_down">';
					$result = $player->prepare("SELECT count(*) FROM player WHERE DATE_SUB(NOW(), INTERVAL $update_players MINUTE) < last_play"); 
					$result->execute(); 
					$number_of_rows = $result->fetchColumn(); 
					print $number_of_rows.' Online hráčů';
				print '</div>';
			}
		?>
		<main>
			<div id="fullpage">
				<div class="section" id="section0">
					<div class="content">
						<div class="slide">
							<h2>Základní informace o hře</h2>
							<div class="cols">
								<div class="text_col">
								Kdysi dávno byla jedna jediná říše, která existovala po celém kontinentu. Země klidu a míru, kde neexistovaly války a nemoci. Lidé tu žili šťastní a v harmonickém soužití.
								Jejich osud se však začal měnit, když z nebe spadl obrovský kámen, Ten začal měnit zvířata v příšery, jeho samotná přítomnost vytvářela smrtelné nemoci, které se šířily po celém světě. Nevinní lidé trpěli stejně jako ti, kteří byli zabiti zvířaty nebo zemřeli na následky nemoci později ožili jako nemrtví. Nemrtví působili zkázu a chaos, který se zdál být nekonečným. Vznikla tím pohroma, která neměla konce a žádného východiska. Nakonec se jediné impérium rozpadlo na dvě různá království, kde všichni bojují za vlastní přežití. Od tohoto velkého dne se k sobě tyto království chovají jako nepřátelé.
								</div>
							</div>
						</div>
					</div>
				</div>	
				<div class="section" id="section1">
					<div class="content">
						<h2>Registrace</h2>
						<?php
							if($register) {
								if (isset($_POST['username'])) {
									$check_login = $account->prepare("SELECT count(*) FROM account WHERE login = '".$_POST['username']."'"); 
									$check_login->execute(); 
									$check_login = $check_login->fetchColumn();
									$check_email = $account->prepare("SELECT count(*) FROM account WHERE email = '".$_POST['email']."'"); 
									$check_email->execute(); 
									$check_email = $check_email->fetchColumn(); 
									if($check_login>0)
										print '<div class="headline">
													<center><font color="red">Toto uživatleské jeméno je již obsazeno</font></center>
												</div>';
									else if($check_email>0)
										print '<div class="headline">
													<center><font color="red">Tento e-mail je již</br></br> registrován</font></center>
												</div>';
									else {
										if(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
											if($_POST['pw'] == $_POST['repeat_pw']) {
												
												$hash = "*" . sha1(sha1($_POST['pw'], true));
												$password = strtoupper($hash);
												if($bonus)
													$expire = "20221218131717"; //Data expirarii sanselor (2022-12-18 13:17:17)
												else
													$expire = "0";
												$sql = "INSERT INTO account(login,
															password,
															social_id,
															email,
															create_time,
															status,
															gold_expire, 
															silver_expire, 
															safebox_expire, 
															autoloot_expire, 
															fish_mind_expire, 
															marriage_fast_expire, 
															money_drop_rate_expire) VALUES (
															:login,
															:password,
															:social_id,
															:email,
															NOW(),
															:status,
															:gold_expire, 
															:silver_expire, 
															:safebox_expire, 
															:autoloot_expire, 
															:fish_mind_expire, 
															:marriage_fast_expire, 
															:money_drop_rate_expire)";
												$stmt = $account->prepare($sql);
												$stmt->bindParam(':login', $_POST['username'], PDO::PARAM_STR);       
												$stmt->bindParam(':password', $password, PDO::PARAM_STR);       
												$stmt->bindParam(':social_id', $_POST['delcode'], PDO::PARAM_STR);       
												$stmt->bindParam(':email', $_POST['email'], PDO::PARAM_STR);       
												$stmt->bindParam(':status', $status_register, PDO::PARAM_STR);       
												$stmt->bindParam(':gold_expire', $expire, PDO::PARAM_STR); 
												$stmt->bindParam(':silver_expire', $expire, PDO::PARAM_STR); 
												$stmt->bindParam(':safebox_expire', $expire, PDO::PARAM_STR); 
												$stmt->bindParam(':autoloot_expire', $expire, PDO::PARAM_STR); 
												$stmt->bindParam(':fish_mind_expire', $expire, PDO::PARAM_STR); 
												$stmt->bindParam(':marriage_fast_expire', $expire, PDO::PARAM_STR); 
												$stmt->bindParam(':money_drop_rate_expire', $expire, PDO::PARAM_STR); 
												$stmt->execute();
												print '<div class="headline">
															<center><font color="green">Tvůj účet byl úspěšně vytvořen! </br></br>Můžeš se přihlásit do hry.</font></center>
														</div>';
											}
											else
												print '<div class="headline">
															<center><font color="red">Hesla se neshodují!</font></center>
														</div>';
										}
										else
											print '<div class="headline">
														<center><font color="red">E-mailová adresa je neplatná!</font></center>
													</div>';
									}
								}
						?>
						<form action="#registration" method="post">
							<input type="text" pattern=".{5,16}" maxlength="16" required="required" name="username" placeholder="Jméno" />
							<div class="reg_info">
								5 a 16 znaků. Musí obsahovat písmena a čísla.
							</div>
							<input type="email" required="required" name="email" placeholder="E-mail" />
							<div class="reg_info">
								Emailová adresa musí být platná.
							</div>
							<input id="reg_pw" pattern=".{5,}" type="password" required="required" name="pw" placeholder="Heslo" />
							<div class="reg_info">
								Minimálně 5 znaků. Nejlepší případ, s velkými a malými písmeny, čísly a speciálními znaky.
							</div>
							<input id="reg_pw2" pattern=".{5,}" type="password" required="required" name="repeat_pw" placeholder="Heslo znovu" />
							<div class="reg_info">
								Zadejte výše uvedené heslo znovu.
							</div>
							<input type="number" min="1000000" max="9999999" required="required" name="delcode" placeholder="Kód pro smazání postavy" id="delcodeInput"/>
							<div class="reg_info">
								Musí obsahovat 7 číslic. Písmena a speciální znaky nejsou povoleny.
							</div>
							<button class="btn" type="submit" name="submit">Registrovat</button>
						<?php
							print '<div class="headline">
									<center><font color="red"> </br></br> Při registraci automaticky dávate souhlas s <a href="#vop">Pravidly</a> </font></center>
									</div>';
						?>
						</form>
						<?php
							}
							else
								print '<div class="headline">
											<center><font color="red">Registrace je momentálně</br></br> Uzavřena</font></center>
										</div>';
						?>
					</div>
				</div>
				<div class="section" id="section2">
					<div class="content">
						<h2>Stažení hry</h2>
						<?php if($download_client)
							print '<div class="headline">
									<center><font color="yellow">Pokud máte problém se spuštěním </br></br>návod zde:<a href="#problems">Řešení problémů clientu</a> </font></center>
									</div>';
						?>	
						<?php if($download_client)
								print "<a href='$download_client' class='btn'>
									Celý herní client
								</a>";
							  if($download_patcher)
								print "<a href='$download_patcher' class='btn'>
									Herní Launcher
								</a>";
						?>						
					</div>
				</div>
				<div class="section" id="section3">
					<div class="content">
						<h2>Žebříček postav</h2>
						<table class="table table-inverse">
						  <thead>
							<tr>
							  <th>#</th>
							  <th>Jméno</th>
							  <th>Říše</th>
							  <th>Cech</th>
							  <th>Úrověn</th>
							  <th>BZK</th>
							</tr>
						  </thead>
						  <tbody>
							<?php
								$stmt  = $player->query("SELECT COUNT(*) as rows FROM player")->fetch(PDO::FETCH_OBJ);
								$total  = $stmt->rows;
								$pages  = ceil($total / $players_rank_on_page);
								$get_pages = isset($_GET['page']) ? $_GET['page'] : 1;
								if($get_pages>$pages)
									$get_pages = 1;
								$x = ($get_pages-1)*$players_rank_on_page;
								$stmt = $player->query("SELECT * FROM player WHERE name NOT LIKE '[%]%' order by level desc,exp desc limit $x ,$players_rank_on_page"); 
								$rank = $x;
									while($user = $stmt->fetchObject()) {
										$rank++;
										$empire = $player->query("SELECT empire FROM player_index WHERE id = $user->account_id");
										$empire = $empire->fetch(PDO::FETCH_ASSOC);
										$empire = $empire['empire'];
										$guild_id = $player->query("SELECT guild_id FROM guild_member WHERE pid = $user->id");
										$guild_id = $guild_id->fetch(PDO::FETCH_ASSOC);
										$guild_id = $guild_id['guild_id'];
										if($guild_id)
										{
											$guild = $player->query("SELECT name FROM guild WHERE id = $guild_id");
											$guild = $guild->fetch(PDO::FETCH_ASSOC);
											$guild = $guild['name'];
										}
										else
											$guild = '-';
										print "<tr>
													<th scope='row'>$rank</th>
													<td>$user->name</td>
													<td><img src='img/empire/$empire.jpg'></td>
													<td>$guild</td>
													<td>$user->level</td>
													<td>$user->exp</td>
												</tr>";
									};
							?>
						  </tbody>
						</table>
						<?php
							if($get_pages>1)
								echo '<a href="?page='.($get_pages-1).'#ranking" class="btn pull-left"> << </a>';
							if($get_pages<$pages)
								echo '<a href="?page='.($get_pages+1).'#ranking" class="btn pull-right"> >> </a>';
						?>
					</div>
				</div>
				<div class="section" id="section4">
					<div class="content">
						<div class="slide">
							<div class="cols">
								<div class="text_col">
								<h2>Pravidla používání</h2>
								<p><br/>
								<h2>Zpracování a ochrana osobních údajů</h2>
								<p><br/>
								<p>Při registraci a příhlášení do herního serveru lorderon se shromažďují údaje a informace, 
									které jsou nezbytné pro funkcionalitu služeb, slouží k rozeznání uživatele a ke správě účtu uživatelem.
								<p><br/>
									Údaje jsou ukládány v serverové databázi, která je chráněna heslem s povoleným přístupem pouze z konkrétní IP adresy správce. Přístup k údajům má pouze subjekt údajů, správce a systém, který s nimi automaticky nakládá v zájmu funkcionality služeb (webová stránka, aplikace).
								<p><br/>
									Zpracování a využití osobních údajů je prováděno automaticky a jeho cílem je zajištění funkčnosti a využitelnosti služeb. Nakládání s osobními údaji probíhá podle zákona o ochraně osobních údajů č. 101/2000 Sb. a nařízení Evropského parlamentu a Rady(EU) 2016/679 o ochraně fyzických osob v souvislosti se zpracováním osobních údajů a poučení subjektů údajů (GDPR)
								<p><br/>
									Zpracovávanými osobními údaji jsou:
									Uživatelské jméno,
									Emailová adresa,
									IP adresa,
									Heslo (V zašifrované podobě).
									<p><br/>
									Doba uložení údajů je na dobu neurčitou.<br/>
								<p><br/>
								<h2>Lorderon GM-Team</h2>
									- Hru moderují námi vybrané osoby
								<p><br/>
									- Moderátoři mají přístup k určitým částem informací
								<p><br/>
									- Moderátoři mají svá pravidla a úkoly
								<p><br/>
									- Moderátoři nemají přístup do databáze účtů a emailů (Do té má přístup pouze systém a Majitel serveru)
								<p><br/>
								<h2>Aplikace třetí strany</h2>
									- Používání takového softwaru je zakázáno a trestáno (rozsah trestu určuje vedení serveru po přezkoumání prohřešku)
								<p><br/>
								<h2>aktualizace herního Klienta</h2>
									- Software, který automaticky aktualizuje soubory hry a umožňuje přístup do hry
								<p><br/>
									- Jakákoliv modifikace je zakázána a trestána
								<p><br/>
									- Patcher stahuje soubory pouze do složky clientu neuhládá ani neodesílá žádné soubory ve vašem systému
								<p><br/>
								<h2>Zneužívání chyb</h2>
									- Vzhledem k obsáhlosti prvků, které se na tomto projektu nachází, se může vyskytnout neočekávaný problém
								<p><br/>
									- V případě nalezení takového problému nás bezodkladně kontaktujte, nenahlášení a zneužívání je trestáno
								<p><br/>
								<h2>Registrace herního účtu</h2>
									- Pro vytvoření uživatelského konta (účtu) músí být splněna určitá kriteria
								<p><br/>
									- Údaje nesmí být nevhodné, pejorativní - v rozporu se zákony ČR (moderátor vás může vyzvat ke změně těchto údajů, upravit Vám je nebo Vás potrestat)
								<p><br/>
									- Uživatelské konto (účet) musí být aktivován do 24. hodin od registrace, v opačném případě bude uživatelské konto odstraněno (Konto aktivujete tak že se přihlásíte do hry)
								<p><br/>
									- Není limitováno množství účtů, které může uživatel vlastnit
								<p><br/>
								<h2>Herní postava</h2>
									- Pro vytvoření herní postavy je nutnost vlastnit uživatelské konto (účet), dále je nutné splňovat určitá kriteria
								<p><br/>
									- Údaje nesmí být nevhodné, pejorativní - v rozporu se zákony ČR (moderátor vás může vyzvat ke změně těchto údajů, upravit Vám je nebo Vás potrestat)
								<p><br/>
								<h2>Pravidla hry</h2>
									- Není povoleno používat programy 3. strany (které zasahují do hry)
								<p><br/>
									- Není povoleno modifikovat hru
								<p><br/>
									- Není povoleno nevhodné chování, pejorativní - v rozporu se zákony ČR a spamování
								<p><br/>
									- Není povoleno obchodování s reálnou měnou (Pouze ve hře - Mimo hru nebude team tyto prohřešky řešit)
								<p><br/>
									- Není povolené meziserverové obchodování (Pouze ve hře - Mimo hru nebude team tyto prohřešky řešit)
								<p><br/>
									- Není povoleno poškozovat dobré jméno služeb portálu, vymýšlet si, lhát nebo uvádět nepřesné informace
								<p><br/>
									- Není povoleno obtěžovat herního moderátora (můžete se ptát na dotazy ohledně hry a kolem hry, na přímé dotazy na moderátora ohledně osobního života nemusí reagovat; žádat ho o věci, kterýma by porušil pravidla pro moderátory)
								<p><br/>
									- Není povoleno obcházet blokaci chatu
								<p><br/>
									- Není povoleno vydávat se za moderátora
									<p><br/>
									- Není povoleno zveřejnovat identitu nebo osobní informace o spoluhráčích nebo moderátorech (jméno, příjmení, věk, bydliště atp.)
								<p><br/>
									- Je povinností spouštět herní klient pouze přes Launcher/Patcher (Lorderon.exe) - Je povinností respektovat moderátora a jeho nařízení
								<p><br/>
									- Je povinností nahlašovat chyby
								<p><br/>
									- Při herní události se může uživatel účastnit pouze herní události pouze jednou (nesmí se účastnit s více postavama)
								<p><br/>
									Porušení jakéhokoli bodu pravidel je zakázáno a trestáno (dle rozsahu prohrešku).<br/>
								</p>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="section" id="section5">
					<div class="content">
						<div class="slide">
							<div class="cols">
								<div class="text_col">
								<h2>Řešení problémů</h2>
								<p><br/>
									<p>Nejde-li Vám spustit hra, znamená to že Vaše zařízení není kompatibilitní s naší hrou.
								<p><br/>
									Můžete Však skusit několik tipů k odstranění problémů, pokud problémy přetrvávají i po vyzkoušení těchto tipů, kontaktujte nás na discordu nebo facebooku kde se Vám pokusíme pomoct.<br/>
								<p><br/>
									Hra nejde spustit?</h2>
								<p><br/>
									1) Spusť launcher s oprávněním administrátora
								<p><br/>
									2 Spusť launcher v režimu kompatibility Windows XP (SP3)
								<p><br/>
									3 Stahněte a nainstalujte všechny opravné balíky najdete je zde: <a href="/files/oprava.rar">Opravný balíček</a>
								<p><br/>	
									4 Vyzkoušejte dočasně deaktivovat Váš antivirový program nebo dočasně deaktivovat FireWall
								<p><br/>	
									5 Nainstalujte Microsoft .NET Framework 3.5+ Zde <a href="https://www.microsoft.com/en-us/download/details.aspx?id=21">MS.net</a>
								<p><br/>	
									6 Je možné že se při stažení clienta stala chyba, proto ho smažte a stáhněte znovu
								<p><br/>	
									Pokud nic nepomohlo kontaktujte nás na discordu zde : <a href="https://discordapp.com/invite/hcd2zet">Discord</a>
								</p>
								</div>
							</div>
						</div>
					</div>
				</div>	
			</div>
		</main>
		<script>
			delcodeInput.oninput = function () {
				if (this.value.length > 7)
					this.value = this.value.slice(0,7); 
			}
		</script>
		<script src="js/lightbox.js"></script>
	</body>
</html>
